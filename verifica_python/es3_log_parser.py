'''
ESERCIZIO 3 — Parsing Log Cloud 

Il programma deve leggere il file access_log.txt contenente righe nel formato:
DATA ORA IP METODO URL STATUS CODE_MS

Il programma deve calcolare e stampare:
1. numero totale richieste
2. numero richieste con status 200
3. numero richieste con status 404
4. IP che ha fatto più richieste
5. tempo medio di risposta (media di CODE_MS)

Output richiesto:
Report log - Studente: <nome>
Totale richieste: ...
Status 200: ...
Status 404: ...
IP più attivo: ...
Tempo medio risposta: ... ms
'''

nome = input("Inserisci il tuo nome: ")  #Federico Podio


tot_richieste = 0
status_200 = 0
status_404 = 0
conteggio_ip = 0
somma_tempi_ms = 0


with open("access_log.txt", 'r') as file: #path in verifica_python
    for linea in file:
        linea = linea.strip()
        if not linea:
            continue  
        parti = linea.split()         
        if len(parti) < 7:
            continue
        ip = parti[2]
        status = parti[5]
        
        try:
            code_ms = int(parti[6])
        except ValueError:
            continue  
        tot_richieste += 1
        conteggio_ip += 1
        somma_tempi_ms += code_ms
        
        if status == "200":
            status_200 += 1
        elif status == "404":
            status_404 += 1

ip_piu_attivo = conteggio_ip if conteggio_ip else "N/A"
t_medio = (somma_tempi_ms / tot_richieste) if tot_richieste > 0 else 0


#output nel formato richiesto
print("Report log - Studente: Federico Podio")
print(f"{nome} - Totale richieste: {tot_richieste}")
print(f"{nome} - Status 200: {status_200}")
print(f"{nome} - Status 404: {status_404}")
print(f"{nome} - IP più attivo: {ip_piu_attivo}")
print(f"{nome} - Tempo medio risposta: {t_medio:.2f} ms")