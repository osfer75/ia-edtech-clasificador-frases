import pandas as pd

df = pd.read_csv("data/frases.csv")
print(df)
print("\nCantidad de frases por nivel:")
print(df["dificultad"].value_counts())
