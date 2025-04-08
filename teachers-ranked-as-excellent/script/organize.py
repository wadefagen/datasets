import pandas as pd

df = pd.read_csv("../uiuc-tre-dataset.csv")

df = df.sort_values("term", ascending=False)

print(df)