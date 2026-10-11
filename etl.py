import pandas as pd

df = pd.read_csv('discos.csv', sep=',')

df['Preço'] = df['Preço'].astype(str).str.replace('R$', '', regex=False)
df['Preço'] = df['Preço'].str.replace(',', '.', regex=False)

df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')

df['Ano'] = df['Ano'].replace(0, pd.NA)

df.to_csv('estoque_limpo.csv', index=False)
print("Dados limpos")