import pandas as pd
from src.config import FILE_TITANIC, HEAD_ROWS, url_titanic

df = pd.read_csv(url_titanic)

print(df.shape,"\n")
print(df.head(HEAD_ROWS),"\n")
print(df.info(), "\n")
print(df.describe(), "\n")

print("\n\n\n\n")
print(df.notna().sum(),"\n")


