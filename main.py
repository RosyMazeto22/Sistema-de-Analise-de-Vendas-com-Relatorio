import pandas as pd

# Carregar dados
df = pd.read_csv("dados.csv")

# Criar faturamento
df["faturamento"] = df["quantidade"] * df["valor"]

print("\n📊 Dados carregados:")
print(df)

# Faturamento total
total = df["faturamento"].sum()
print(f"\n💰 Faturamento total: R$ {total}")

# Vendas por categoria
categoria = df.groupby("categoria")["faturamento"].sum()
print("\n📦 Faturamento por categoria:")
print(categoria)

# Produto mais vendido
produto = df.groupby("produto")["quantidade"].sum().idxmax()
print(f"\n🏆 Produto mais vendido: {produto}")