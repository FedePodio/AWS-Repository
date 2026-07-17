"""
------------------------------------------------------------------------------
    Programma di virtualizzazione di schede per allenamento in palestra
------------------------------------------------------------------------------
"""

import curses # per interfaccia testuale
import json
import locale
from pathlib import Path

DATA_FILE = Path.home()/".schede_allenamento.json"

GIORNI = [
    ("lun", "Lunedi"),
    ("mar", "Martedi"),
    ("mer", "Mercoledi"),
    ("gio", "Giovedi"),
    ("ven", "Venerdi"),
    ("sab", "Sabato"),
    ("dom", "Domenica"),
]
# ------------------------------------------------------------------------

# Persistenza (ricorda info anche dopo aver spento il programma)
def load_data() -> dict:
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text("utf-8"))
        except Exception:
            return {}
    return {}

def save_data(data: dict) -> None:
    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), "utf-8")

def parse_exercises(raw: str):
    exercises = []
    for entry in raw.split(";"):
        entry = entry.strip()
        if not entry:
            continue
        parts = [p.strip() for p in entry.split("-", 3)] # split su "-"
        if len(parts) != 4:
            return None, (
                f"Formato non valido: '{entry}'\n"
                "  Usa: nomeEsercizio-serie-ripetizioni-carico"
            )
        nome, serie, rip, carico = parts
        if not nome:
            return None, # Il nome dell'es non può essere vuoto
        exercises.append({
            "nome": nome,
            "serie": serie,
            "ripetizioni": rip,
            "carico": carico,
        })
    if not exercises:
        return None, "Nessun esercizio inserito."
    return exercises, None
# ------------------------------------------------------------------------
# ID color pair
P_TITLE = 1    # cyan
P_SEL = 2    # black w cyan
P_HEAD = 3    # yellow
P_OK = 4    # green
P_ERR = 5    # red
P_BORDER = 6    # blue
P_DIM = 7    # white
# ------------------------------------------------------------------------

# Primitivi
def init_colors() -> None: # curses
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(P_TITLE, curses.COLOR_CYAN, -1) #associa a un ID una combinazione di colore di testo/sfondo
    curses.init_pair(P_SEL, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(P_HEAD, curses.COLOR_YELLOW, -1)
    curses.init_pair(P_OK, curses.COLOR_GREEN, -1)
    curses.init_pair(P_ERR, curses.COLOR_RED, -1)
    curses.init_pair(P_BORDER, curses.COLOR_BLUE, -1)
    curses.init_pair(P_DIM, curses.COLOR_WHITE, -1)

def _ch(win, y, x, ch, attr=0): # Stampa un ch alle coordinate y/x applicando stile(attr)
    H, W = win.getmaxyx()   # Controlla che le coordinate siano all'interno di altezza/larghezza
    if 0 <= y < H and 0 <= x < W:
        try:
            win.addch(y, x, ch, attr)
        except curses.error:
            pass

def _str(win, y, x, text, attr=0): # non fa uscire testo dal riquadro
    H, W = win.getmaxyx()
    if y < 0 or y >= H or x >= W:
        return
    avail = W - x - 1
    if avail <= 0:
        return
    try:
        win.addstr(y, x, text[:avail], attr)
    except curses.error:
        pass

def draw_box(win, y, x, h, w, title="", pair=P_BORDER): # Disegna rettangolo con dimensioni h/w
    a = curses.color_pair(pair)
    _ch(win, y, x, curses.ACS_ULCORNER, a) # angoli
    _ch(win, y, x+w-1, curses.ACS_URCORNER, a)
    _ch(win, y+h-1, x, curses.ACS_LLCORNER, a)
    _ch(win, y+h-1, x+w-1, curses.ACS_LRCORNER, a)
    for i in range(1, w-1):
        _ch(win, y, x+i, curses.ACS_HLINE, a) # ____
        _ch(win, y+h-1, x+i, curses.ACS_HLINE, a)
    for i in range(1, h-1):
        _ch(win, y+i, x, curses.ACS_VLINE, a)
        _ch(win, y+i, x+w-1, curses.ACS_VLINE, a)
    # if title:
    #     t = f" {title} "
    #     tx = x + max(1, (w - len(t)) // 2)
    #     _str(win, y, tx, t, a | curses.A_BOLD)

def draw_hline(win, y, x, w, pair=P_BORDER): # linea lunga "w" coord yx
    a = curses.color_pair(pair)
    for i in range(w):
        _ch(win, y, x+i, curses.ACS_HLINE, a)

def center_str(win, y, text, attr=0): # centrare roba
    _, W = win.getmaxyx()
    x = max(0, (W - len(text)) // 2)
    _str(win, y, x, text, attr)

def status_bar(win, msg, pair=P_DIM): #status bar = indicazioni per user("frecce su giu, usa x per andare avanti, etc...")
    H, W = win.getmaxyx()
    bar = msg.ljust(W)[:W]
    try:
        win.addstr(H-1, 0, bar, curses.color_pair(pair) | curses.A_REVERSE)
    except curses.error:
        pass
# ------------------------------------------------------------------------

# Text input
def read_line(win, y, x, max_len=400) -> str | None:
    H, W = win.getmaxyx() # dimensioni max finestra testo in terminale
    buf: list[str] = [] # lista vuota per user
    curses.curs_set(1) # cursore visibile
    win.move(y, x)
    win.refresh()

    while True:
        try:
            ch = win.get_wch() # tasto a/1/@ = CH | tasto speciale(frecce) = INT
        except Exception:
            continue

        if isinstance(ch, str): # CH
            if ch == "\x1b": # ESC, interrompe f
                curses.curs_set(0)
                return None
            elif ch in ("\n", "\r"): # INVIO, esce e salva
                break
            elif ch in ("\x7f", "\x08"): # BACK/DEL, visual clarity
                if buf:
                    buf.pop() # scambia ultimo ch con spazio vuoto (visual only)
                    cy, cx = win.getyx()
                    if cx > x:
                        _str(win, cy, cx-1, " ")
                        win.move(cy, cx-1)
                        
            elif ord(ch) >= 32 and len(buf) < max_len: # input user visibile (esercizi)
                col = x + len(buf)
                if col < W - 2:
                    buf.append(ch)
                    _str(win, y, col, ch)
                    win.move(y, col + 1)

        elif isinstance(ch, int): # INT
            if ch == curses.KEY_BACKSPACE:
                if buf:
                    buf.pop()
                    cy, cx = win.getyx()
                    if cx > x:
                        _str(win, cy, cx-1, " ")
                        win.move(cy, cx-1)
            elif ch in (10, 13): # INVIO
                break
            elif ch == 27: # ESC
                curses.curs_set(0)
                return None

        win.refresh()

    curses.curs_set(0)
    return "".join(buf) # salva in str unica/singola
# ------------------------------------------------------------------------

# Render tabella
def draw_exercise_table(win, exercises: list, y: int, x: int, w: int) -> int:
    if not exercises:
        _str(win, y, x, "  Nessun esercizio registrato.", curses.color_pair(P_DIM))
        return y + 2
    
    nome_ver  = max(len("Esercizio"), max(len(e["nome"]) for e in exercises)) + 1
    serie_ver = max(len("Serie"), max(len(e["serie"]) for e in exercises)) + 1
    ripetizione_ver   = max(len("Rip."), max(len(e["ripetizioni"]) for e in exercises)) + 1
    carico_ver   = max(len("Carico"), max(len(e["carico"]) for e in exercises)) + 1

    def row_str(nome, serie, rip, carico):
        return (
            f"{nome:<{nome_ver}}"
            f"{serie:^{serie_ver}}"
            f"{rip:^{ripetizione_ver}}"
            f"{carico:^{carico_ver}}"
        )

    hdr = row_str("Esercizio", "Serie", "Rip.", "Carico") # Header
    _str(win, y, x, hdr, curses.color_pair(P_HEAD) | curses.A_BOLD)
    draw_hline(win, y+1, x, min(len(hdr)+2, w))

    for i, ex in enumerate(exercises):
        row = row_str(ex["nome"], ex["serie"], ex["ripetizioni"], ex["carico"])
        alt = curses.A_DIM if i % 2 == 0 else 0
        _str(win, y+2+i, x, row, curses.color_pair(P_DIM) | alt)

    return y + 2 + len(exercises) + 1
# ------------------------------------------------------------------------

# Entry point "app"
def screen_main_menu(win) -> str | None: # Main menu ->view/register/quit
    idx = 0
    # lista tuple menu
    options = [ 
        ("[V]  Visualizza scheda",  "view"),    # opzioni menu iniziale
        ("[R]  Registra scheda",    "register"),
        ("[Q]  Esci",               None),
    ]

    while True:         # calcola la geometria menu per rimanere centrato
        win.clear()     # anche se l'utente ridimensiona il terminale
        H, W = win.getmaxyx()
        bw = min(W - 4, 56) #larghezza box del menu "bw" max 56 ch
        bx = max(0, (W - bw) // 2)  # coordinata X di partenza (centr. orizz)
        draw_box(win, 1, bx, H - 3, bw, "", P_BORDER)

        # grafica titolo
        logo_y = 2
        _str(win, logo_y, bx + 4, "SCHEDE DI ALLENAMENTO",
             curses.color_pair(P_TITLE) | curses.A_BOLD) # titolo grassetto
        _str(win, logo_y + 1, bx + 4, "Gestione schede di palestra",
             curses.color_pair(P_DIM))  # sottotitolo opaco
        draw_hline(win, logo_y + 2, bx + 1, bw - 2, P_BORDER) #linea separa

        menu_y = logo_y + 4
        for i, (label, _) in enumerate(options): # cicla lungo le opzioni per stamparle una sotto l'altra
            if i == idx:
                attr = curses.color_pair(P_SEL) | curses.A_BOLD # testo cyan sfondo nero
                prefix = " > "
            else:
                attr = curses.color_pair(P_DIM)
                prefix = "   "
            _str(win, menu_y + i * 2, bx + 3, f"{prefix}{label}   ", attr) # menu_y + i * 2 -> dist 2 righe

        _str(win, H - 4, bx + 3, "  Usa frecce SU/GIU' + INVIO oppure i tasti tra parentesi", curses.color_pair(P_DIM))

        status_bar(win, "  Frecce ↑↓ + INVIO per navigare  |  Q per uscire")
        win.refresh()

        ch = win.getch() # attesa input user
        if ch == curses.KEY_UP: # sposta riga scelta
            idx = (idx - 1) % len(options)
        elif ch == curses.KEY_DOWN:
            idx = (idx + 1) % len(options)
        elif ch in (10, 13): # invio
            return options[idx][1]
        elif ch in (ord("q"), ord("Q"), 27):
            return None
        elif ch in (ord("v"), ord("V")):
            return "view"
        elif ch in (ord("r"), ord("R")):
            return "register"


def screen_day_selector(win, data: dict, mode: str) -> str | None: 
    idx = 0
    title = "VISUALIZZA SCHEDA" if mode == "view" else "REGISTRA SCHEDA"
    subtitle = (
        "Seleziona il giorno da visualizzare:"
        if mode == "view"
        else "Seleziona il giorno da registrare:"
    )

    while True:
        win.clear()
        H, W = win.getmaxyx()
        bw = min(W - 4, 54)
        bx = max(0, (W - bw) // 2)
        draw_box(win, 1, bx, H - 3, bw, title, P_TITLE) # centra e calcola dim box

        _str(win, 3, bx + 3, f"  {subtitle}", curses.color_pair(P_HEAD))
        draw_hline(win, 4, bx + 1, bw - 2)

        for i, (key, label) in enumerate(GIORNI): # crea elenco giorni
            has = key in data
            marker = "[*]" if has else "[ ]"
            note   = "  (scheda presente)" if has else ""
            row    = f"  {marker}  {label}{note}"

            if i == idx:
                attr = curses.color_pair(P_SEL) | curses.A_BOLD # txt grassetto dove sta il cursore
            elif has:
                attr = curses.color_pair(P_OK) # verde
            else:
                attr = curses.color_pair(P_DIM) # w/grey

            _str(win, 5 + i, bx + 3, f"{row:<{bw-5}}", attr) # stampa str con spazi a fine

        draw_hline(win, 5 + len(GIORNI), bx + 1, bw - 2)
        _str(win, 5 + len(GIORNI) + 1, bx + 3,
             "  [ESC] Torna al menu principale",
             curses.color_pair(P_DIM))
        # Se il giorno ha già dei dati salvati (has = True), l'interfaccia mostra un asterisco 
        # e la scritta (scheda presente). Altrimenti mostra casella vuota
        legend = "  [*] = scheda salvata" if any(k in data for k, _ in GIORNI) else ""
        status_bar(win, f"  Frecce ↑↓ + INVIO  |  ESC Indietro  {legend}")
        win.refresh()

        ch = win.getch()
        if ch == curses.KEY_UP:
            idx = (idx - 1) % len(GIORNI)
        elif ch == curses.KEY_DOWN:
            idx = (idx + 1) % len(GIORNI)
        elif ch in (10, 13):
            return GIORNI[idx][0]
        elif ch == 27:
            return None


def screen_view_card(win, data: dict, day_key: str) -> None:

    day_label = next(l for k, l in GIORNI if k == day_key) # recupero nome gg
    win.clear() # pulisce schermata
    H, W = win.getmaxyx()
    bw = min(W - 4, 72) # crea box
    bx = max(0, (W - bw) // 2)
    draw_box(win, 1, bx, H - 3, bw, f"SCHEDA  {day_label.upper()}", P_TITLE) #SCHEDA LUNEDI

    if day_key not in data: # se la scheda non esiste ancora
        center_str(win, H // 2,
                   f"Nessuna scheda registrata per {day_label}.",
                   curses.color_pair(P_ERR) | curses.A_BOLD)
        center_str(win, H // 2 + 1, "Usa 'Registra scheda' per aggiungerne una.", curses.color_pair(P_DIM))
        # stampa a metà schermo in rosso/ evidenziato
    
    else:                   # se esiste
        exercises = data[day_key]
        n = len(exercises)
        draw_exercise_table(win, exercises, 3, bx + 2, bw - 4) # richiama f ext per tabella
        _str(win, 3 + n + 3, bx + 3,
             f"  Totale: {n} esercizi",
             curses.color_pair(P_DIM) | curses.A_BOLD)

    _str(win, H - 4, bx + 3, "  Premi un tasto qualsiasi per tornare...", curses.color_pair(P_DIM)) # istruzioni uscita
    status_bar(win, f"  Scheda {day_label}  |  Qualsiasi tasto per tornare")
    win.refresh()
    win.getch()

def screen_register_card(win, data: dict, day_key: str) -> bool:
    day_label = next(l for k, l in GIORNI if k == day_key) # lun -> lunedi etc
    overwrite = day_key in data

    while True: # pulisce la finestra e calcola le dimensioni del box di input perchè sia centrato
        win.clear()
        H, W = win.getmaxyx()
        bw = min(W - 4, 76)
        bx = max(0, (W - bw) // 2)
        draw_box(win, 1, bx, H - 3, bw,
                 f"REGISTRA SCHEDA  {day_label.upper()}", P_TITLE)

        row = 3 # stampa 2 righe rosse di avvertimento e sposta l'indice in basso di 3
        if overwrite:
            _str(win, row, bx + 3,
                 "  ATTENZIONE: esiste gia' una scheda per questo giorno!",
                 curses.color_pair(P_ERR) | curses.A_BOLD)
            _str(win, row + 1, bx + 3,
                 "  Proseguendo la scheda esistente verra' sovrascritta.",
                 curses.color_pair(P_ERR))
            row += 3

        _str(win, row, bx + 3,
             "  Formato:  nomeEsercizio-serie-ripetizioni-carico",
             curses.color_pair(P_HEAD) | curses.A_BOLD)
        _str(win, row + 1, bx + 3,
             "  Separa piu' esercizi con il punto e virgola ( ; )",
             curses.color_pair(P_DIM))
        _str(win, row + 2, bx + 3,
             "  Esempio:  Squat-4-8-80kg ; Panca-3-10-60kg ; Stacchi-4-6-100kg",
             curses.color_pair(P_DIM))
        draw_hline(win, row + 4, bx + 1, bw - 2)

        prompt_label = "  > "
        _str(win, row + 5, bx + 3,
             prompt_label,
             curses.color_pair(P_OK) | curses.A_BOLD)

        # Clear input field
        input_x = bx + 3 + len(prompt_label) # ripulisce riga prima di rimpiazzare testo
        _str(win, row + 5, input_x, " " * (bw - (input_x - bx) - 4))

        status_bar(win, "  Digita esercizi e premi INVIO  |  ESC per annullare")
        win.refresh()

        raw = read_line(win, row + 5, input_x, max_len=500)

        if raw is None:         # ESC annulla
            return False

        raw = raw.strip() # toglie spazi
        if not raw: # invio senza scrivere = errore, poi riparte su input
            _str(win, row + 7, bx + 3,
                 "  Errore: nessun dato inserito. Premi un tasto per riprovare.",
                 curses.color_pair(P_ERR))
            win.refresh()
            win.getch()
            continue

        exercises, err = parse_exercises(raw) # spezza str su - ;
        if err:
            _str(win, row + 7, bx + 3,
                 f"  Errore: {err}",
                 curses.color_pair(P_ERR))
            _str(win, row + 8, bx + 3,
                 "  Premi un tasto per riprovare...",
                 curses.color_pair(P_DIM))
            win.refresh()
            win.getch()
            continue

        # Show confirmation screen
        confirmed = screen_confirm_card(win, day_label, exercises, overwrite) # tabella riassuntiva
        if confirmed:
            data[day_key] = exercises
            save_data(data)
            screen_success(win, day_label)
            return True
        # else: loop back/ user re-edit

# sistema save t/f
def screen_confirm_card(win, day_label: str, exercises: list, overwrite: bool) -> bool:
    while True:
        win.clear()
        H, W = win.getmaxyx()
        bw = min(W - 4, 72)
        bx = max(0, (W - bw) // 2)
        title = f"CONFERMA  {day_label.upper()}"
        if overwrite:
            title += "  [SOVRASCRITTURA]"
        draw_box(win, 1, bx, H - 3, bw, title, P_HEAD) # aggiunge messaggio se sovrascrive

        _str(win, 3, bx + 3,
             "  Riepilogo esercizi da salvare:",
             curses.color_pair(P_HEAD) | curses.A_BOLD)
        draw_hline(win, 4, bx + 1, bw - 2)

        draw_exercise_table(win, exercises, 5, bx + 2, bw - 4) # riimpaginazione

        draw_hline(win, H - 8, bx + 1, bw - 2)

        if overwrite:
            _str(win, H - 7, bx + 3,
                 "  La scheda esistente verra' sovrascritta!",
                 curses.color_pair(P_ERR) | curses.A_BOLD)

        _str(win, H - 5, bx + 3,
             "  Confermi il salvataggio?",
             curses.color_pair(P_DIM) | curses.A_BOLD)

        _str(win, H - 4, bx + 3,
             "  [S]  Si, salva      ",
             curses.color_pair(P_OK) | curses.A_BOLD | curses.A_REVERSE) # a_rev inverte colore
        _str(win, H - 4, bx + 24,
             "  [N]  No, modifica   ",
             curses.color_pair(P_ERR) | curses.A_BOLD) # rosso/ grassetto

        status_bar(win, "  S = Salva  |  N / ESC = Torna alla modifica") 
        win.refresh()

        ch = win.getch() # progr. aspetta input
        if ch in (ord("s"), ord("S"), 10, 13): # invio
            return True
        elif ch in (ord("n"), ord("N"), 27): # esc
            return False


def screen_success(win, day_label: str) -> None:
    H, W = win.getmaxyx()
    bw = 46 # w
    bh = 7 # h
    bx = max(0, (W - bw) // 2) # centrare coord x
    by = max(0, (H - bh) // 2) # centrare coord y

    win.clear() # pulisce schermo
    draw_box(win, by, bx, bh, bw, "SALVATO", P_OK) # ricrea di nuovo il rettangolo
    center_str(win, by + 2,
               f"Scheda di {day_label} salvata con successo!",
               curses.color_pair(P_OK) | curses.A_BOLD)
    center_str(win, by + 4,
               "Premi un tasto per continuare...",
               curses.color_pair(P_DIM))
    status_bar(win, "  Scheda salvata!")
    win.refresh()
    win.getch()
# ------------------------------------------------------------------------

# Entry point 

def main(win) -> None:
    init_colors()
    curses.curs_set(0) # nasconde cursore
    win.keypad(True) # frecce

    while True:
        data = load_data()
        action = screen_main_menu(win)

        if action is None: # esci con esc/q -> action diventa none
            break

        elif action == "view":
            while True:
                data = load_data()
                day_key = screen_day_selector(win, data, "view") # torna a schermata giorno
                if day_key is None:
                    break
                screen_view_card(win, data, day_key)

        elif action == "register":
            while True:
                data = load_data()
                day_key = screen_day_selector(win, data, "register")
                if day_key is None:
                    break
                screen_register_card(win, data, day_key)


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt: # es. ctrl c per chiudere -> no crash error
        pass
    print("\nArrivederci!")