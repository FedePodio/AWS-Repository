
voti = [25,28,24,27,29,30,18,25]

def incrementa_voto(v: int):
    return v + 1
# V1
# voti_plus = list(map(incrementa_voto, voti))

# V2
# for voto in voti:
#     voto += 1
#     voti_plus.append(voto)

# V3
# voti_plus = list(map(lambda v: v+1, voti))

# V4
voti_plus = [v+1 for v in voti]

print(voti_plus)

voti_plus_plus = list(filter(lambda v: v > 24, voti))
voti_plus_plus = [v for v in voti if v > 24]
print(voti_plus_plus)
