import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

url = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_1.csv"
url2 = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_2.csv"
url3 = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_3.csv"
url4 = "C:/Users/rannygf/Desktop/Challenge Alura Store/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

Lojas = ['Loja 1','Loja 2','Loja 3','Loja 4']


# Cria a figura
fig = plt.figure(figsize=(18, 9))
fig.canvas.manager.set_window_title("Dashboard Alura Store")
plt.suptitle("Análise Alura Store", fontsize=18, fontweight='bold')

# Maximiza a janela
manager = plt.get_current_fig_manager()
try:
    manager.window.state('zoomed')  # Funciona no TkAgg (Windows)
except:
    try:
        manager.window.showMaximized()  # Funciona no Qt5Agg
    except:
        pass  # Se não funcionar, ignora

#Faturamento

fat1 = loja["Preço"].sum()
fat2 = loja2["Preço"].sum()
fat3 = loja3["Preço"].sum()
fat4 = loja4["Preço"].sum()

Faturamento = [fat1,fat2,fat3,fat4]

plt.subplot(2,3,1)
barras = plt.bar(Lojas, Faturamento, color='skyblue')

for barra in barras:
    valor = int(barra.get_height())
    plt.text(barra.get_x() + barra.get_width() / 2,
             barra.get_height() + 10000,  # Pequeno deslocamento acima da barra
             f'{valor:,}'.replace(',', '.'),  # Formato brasileiro com ponto
             ha='center', va='bottom', fontsize=10)

plt.ylim(min(Faturamento) * 0.95, max(Faturamento) * 1.05)
plt.title('Faturamento das Lojas')
plt.ylabel('Faturamento (R$)')

# # Vendas por Categoria

cat1 = loja.groupby("Categoria do Produto")["Preço"].sum()
cat2 = loja2.groupby("Categoria do Produto")["Preço"].sum()
cat3 = loja3.groupby("Categoria do Produto")["Preço"].sum()
cat4 = loja4.groupby("Categoria do Produto")["Preço"].sum()
Categorias = [cat1,cat2,cat3,cat4]

todas_categorias = sorted(set(cat1.index) | set(cat2.index) | set(cat3.index) | set(cat4.index))

valores_loja1 = [cat1.get(categoria, 0) for categoria in todas_categorias]
valores_loja2 = [cat2.get(categoria, 0) for categoria in todas_categorias]
valores_loja3 = [cat3.get(categoria, 0) for categoria in todas_categorias]
valores_loja4 = [cat4.get(categoria, 0) for categoria in todas_categorias]

totais_categoria = np.array(valores_loja1) + np.array(valores_loja2) + np.array(valores_loja3) + np.array(valores_loja4)

x = np.arange(len(todas_categorias))

plt.subplot(2,3,2)

b1 = plt.bar(x, valores_loja1, label='Loja 1')
b2 = plt.bar(x, valores_loja2, bottom=valores_loja1, label='Loja 2')
b3 = plt.bar(x, valores_loja3, bottom=np.array(valores_loja1) + np.array(valores_loja2), label='Loja 3')
b4 = plt.bar(
    x,
    valores_loja4,
    bottom=np.array(valores_loja1) + np.array(valores_loja2) + np.array(valores_loja3),
    label='Loja 4'
)
    
for i, total in enumerate(totais_categoria):
    plt.text(x[i], total + 5000, f'{total:,.0f}', ha='center', va='bottom', fontsize=10)

plt.xticks(x, todas_categorias, rotation=45, ha='right')
plt.ylabel("Faturamento Total (R$)")
plt.title("Faturamento por Categoria")
plt.legend()

#Avaliação Média por Loja
Avaliacao1 = loja["Avaliação da compra"].mean()
Avaliacao2 = loja2["Avaliação da compra"].mean()
Avaliacao3 = loja3["Avaliação da compra"].mean()
Avaliacao4 = loja4["Avaliação da compra"].mean()

avaliacoes = [Avaliacao1,Avaliacao2,Avaliacao3,Avaliacao4]

plt.subplot(2, 3, 3)
plt.barh(Lojas, avaliacoes, color='skyblue')
plt.title('Média de Avaliação por Loja')
plt.xlabel('Nota média')
plt.xlim(3, 5)

for i, val in enumerate(avaliacoes):
    plt.text(val + 0.05, i, f'{val:.2f}', va='center')

#Quantidade de Vendas por Loja

Vendas = (len(loja),len(loja2),len(loja3),len(loja4))

plt.subplot(2, 3, 4)
plt.pie(Vendas, labels=Lojas, autopct='%1.1f%%', startangle=90)
plt.title('Quantidade de Vendas por Loja')

#Média de Valor da Venda
Media1 = loja["Preço"].mean()
Media2 = loja2["Preço"].mean()
Media3 = loja3["Preço"].mean()
Media4 = loja4["Preço"].mean()

print(round(Media1))


#Média de Valor de Frete


plt.tight_layout()  # Ajusta para não sobrepor títulos/labels

plt.show()
