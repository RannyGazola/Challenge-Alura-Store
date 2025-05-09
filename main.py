import pandas as pd
import matplotlib.pyplot as plt

url = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_1.csv"
url2 = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_2.csv"
url3 = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_3.csv"
url4 = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja.head()

plt.figure(figsize=(10,8))

fat1 = loja["Preço"].sum()
fat2 = loja2["Preço"].sum()
fat3 = loja3["Preço"].sum()
fat4 = loja4["Preço"].sum()
    
# print('Loja 1: ',fat,' - Loja 2:',fat2,' - Loja 3: ',fat3,' - Loja 4: ',fat4)
Lojas = ['Loja 1','Loja 2','Loja 3','Loja 4']
Faturamento = [fat1,fat2,fat3,fat4]

plt.subplot(2,2,1)
plt.bar(Lojas, Faturamento)
plt.ylim(1000000,1600000)
plt.title('Faturamento das Lojas')
plt.ylabel('Faturamento')
#plt.show()

## Vendas por Categoria

# Agrupar por loja e categoria e contar o número de vendas (linhas) por grupo
cat1 = loja.groupby("Categoria do Produto")["Preço"].sum()
cat2 = loja2.groupby("Categoria do Produto")["Preço"].sum()
cat3 = loja3.groupby("Categoria do Produto")["Preço"].sum()
cat4 = loja4.groupby("Categoria do Produto")["Preço"].sum()

Categorias = cat1
#print(cat1["Categoria do Produto"])
#print(type(cat1))
    
# plt.subplot(2,2,2)
# plt.bar(Categorias)
# #plt.show()

# type(Categorias)

import matplotlib.pyplot as plt
import numpy as np

# Categorias de produtos
categorias = [
    "brinquedos", "eletrodomesticos", "eletronicos", "esporte e lazer",
    "instrumentos musicais", "livros", "moveis", "utilidades domesticas"
]

# Vendas por loja em cada categoria (valores fictícios como exemplo)
loja1 = [5000, 120000, 150000, 10000, 30000, 3000, 80000, 4000]
loja2 = [6000, 110000, 130000, 12000, 35000, 2500, 70000, 3000]
loja3 = [4500, 130000, 140000, 15000, 27000, 2000, 60000, 3500]
loja4 = [5500, 125000, 152000, 14000, 29500, 3200, 72000, 3800]

# Configurar posições
x = np.arange(len(categorias))
largura = 0.2

# Plotar
plt.figure(figsize=(14, 6))
plt.bar(x - 1.5*largura, loja1, width=largura, label='Loja 1')
plt.bar(x - 0.5*largura, loja2, width=largura, label='Loja 2')
plt.bar(x + 0.5*largura, loja3, width=largura, label='Loja 3')
plt.bar(x + 1.5*largura, loja4, width=largura, label='Loja 4')

# Estética
plt.xticks(x, categorias, rotation=45, ha='right')
plt.ylabel("Total de Vendas (R$)")
plt.title("Vendas por Categoria em Cada Loja")
plt.legend()
plt.tight_layout()
plt.show()
