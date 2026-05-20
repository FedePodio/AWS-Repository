import pandas as pd

df = pd.read_csv('movie_genre_classification_final.csv')

df_ita = df[df["Language"] == "Spanish"]

df_ita.plot()

