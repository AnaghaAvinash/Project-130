import pandas as pd
import csv

df = pd.read_csv("bright_stars.csv")
del df["Luminosity"]
print(df.shape)

df.to_csv("final.csv")