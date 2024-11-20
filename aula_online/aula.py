# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dados_sobre_casas.csv")

# Atualiza o status dos pedidos na lista
print(df.head(5))

# %%
sns.displot(df.valor_casa, kde=True, aspect=2)

# %%
df.valor_casa.describe().astype(str)

# %%
sns.displot(df.salario_medio_moradores_regiao, kde=True, aspect=2)

# %%
