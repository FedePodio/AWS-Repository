#innstallare pip pandas

import pandas as pd

df_auto = pd.read_csv("auto_csv")
df = pd.read_json("moto.json")

# print(df.tail(3))
# print(df.shape)

moto_sopra_10k = df[df["Prezzo (€)"] > 10000][["Marca", "Modello", "Prezzo "]]
#etc

veicoli = pd.concat([df_auto, df])
print(veicoli)

