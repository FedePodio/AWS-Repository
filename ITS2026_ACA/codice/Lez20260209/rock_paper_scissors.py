import random

simboli = ['rock', 'paper', 'scissors']

umano = input(f"Umano! Scegli tra {simboli} ")
macchina = random.choice(simboli)


print(f"la macchina ha scelto {macchina}")
print(f"l' umano ha scelto {umano}")

if umano == macchina:
    print(f"Entrambi avete scelto {umano}, pareggio")
elif umano == "rock":
    if macchina != "paper":
        print("hai vinto")
    else:
        print("hai perso")
elif umano == "paper":
    if macchina != "scissor":
        print("hai vinto")
    else:
        print("hai perso")
elif umano == "scissor":
    if macchina != "rock":
        print("hai vinto")
    else:
        print("hai perso")