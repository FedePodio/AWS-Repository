#       0  1  2  3  4
voti = [28,25,26,29,30]

totale = 0

quantity = len(voti)

# print(quantity)

# for i in range(quantity):
#     print(i, voti[i])

for voto in voti:
    print(voto)
    #totale = totale + voto
    totale += voto

print(f"Il totale dei voti è {totale}")
print(f"La media è {totale / quantity}")