import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"


loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

def produto_mais_vendido(df, nome_loja):
    contagem = df["Produto"].value_counts()
    produtoMax = contagem.idxmax()
    quantidadeMax = contagem.max()
    produtoMin = contagem.idxmin()
    quantidadeMin = contagem.min()
    produtosMaxMin = ((produtoMax,produtoMin),(quantidadeMax,quantidadeMin))
    return produtosMaxMin

Lojas = ['Loja 1','Loja 2','Loja 3','Loja 4']



fig = plt.figure(figsize=(18, 9))
fig.canvas.manager.set_window_title("Dashboard Alura Store")
plt.suptitle("Análise Alura Store", fontsize=18, fontweight='bold')


manager = plt.get_current_fig_manager()
try:
    manager.window.state('zoomed')
except:
    try:
        manager.window.showMaximized()
    except:
        pass

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
             barra.get_height() + 10000,
             f'{valor:,}'.replace(',', '.'),
             ha='center', va='bottom', fontsize=10)

plt.ylim(min(Faturamento) * 0.95, max(Faturamento) * 1.05)
plt.title('Faturamento das Lojas')
plt.ylabel('Faturamento (R$)')

# Vendas por Categoria

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

maisVendido1 = produto_mais_vendido(loja, "Loja 1")
maisVendido2 = produto_mais_vendido(loja2, "Loja 2")
maisVendido3 = produto_mais_vendido(loja3, "Loja 3")
maisVendido4 = produto_mais_vendido(loja4, "Loja 4")

plt.subplot(2, 3, 4)
plt.title('Produtos Campeões de Vendas')
plt.text(
    0.5, 0.9,
    f"Loja 1:",
    ha='center', va='center', fontsize=10, wrap=True, fontweight = 'bold' 
)
plt.text(
    0.5, 0.8,
    f"Mais vendido: {maisVendido1[0][0]} ({maisVendido1[1][0]} unidades)\n Menos vendido: {maisVendido1[0][1]} ({maisVendido1[1][1]} unidades).",
    ha='center', va='center', fontsize=10, wrap=True
)
plt.text(
    0.5, 0.7,
    f"Loja 2:",
    ha='center', va='center', fontsize=10, wrap=True, fontweight = 'bold' 
)
plt.text(
    0.5, 0.6,
    f"Mais vendido: {maisVendido2[0][0]} ({maisVendido2[1][0]} unidades)\n Menos vendido: {maisVendido2[0][1]} ({maisVendido2[1][1]} unidades).",
    ha='center', va='center', fontsize=10, wrap=True
)
plt.text(
    0.5, 0.5,
    f"Loja 3:",
    ha='center', va='center', fontsize=10, wrap=True, fontweight = 'bold' 
)
plt.text(
    0.5, 0.4,
    f"Mais vendido: {maisVendido3[0][0]} ({maisVendido3[1][0]} unidades)\n Menos vendido: {maisVendido3[0][1]} ({maisVendido3[1][1]} unidades).",
    ha='center', va='center', fontsize=10, wrap=True
)
plt.text(
    0.5, 0.3,
    f"Loja 4:",
    ha='center', va='center', fontsize=10, wrap=True, fontweight = 'bold' 
)
plt.text(
    0.5, 0.2,
    f"Mais vendido: {maisVendido4[0][0]} ({maisVendido4[1][0]} unidades)\n Menos vendido: {maisVendido4[0][1]} ({maisVendido4[1][1]} unidades).",
    ha='center', va='center', fontsize=10, wrap=True
)
plt.axis('off')


#Média de Valor de Frete
Frete1 = loja["Frete"].mean()
Frete2 = loja2["Frete"].mean()
Frete3 = loja3["Frete"].mean()
Frete4 = loja4["Frete"].mean()

Fretes = (Frete1 , Frete2 , Frete3 , Frete4)

plt.subplot(2,3,5)
barrasFretes = plt.bar(Lojas, Fretes, color = 'skyblue')
plt.bar_label(barrasFretes, fmt='R$ %.0f', padding=2, fontsize=10)
plt.ylim(min(Fretes) * 0.95, max(Fretes) * 1.05)
plt.title('Valor Frete em Média')


#Média de Valor da Venda
Media1 = loja["Preço"].mean()
Media2 = loja2["Preço"].mean()
Media3 = loja3["Preço"].mean()
Media4 = loja4["Preço"].mean()

Medias = (Media1 , Media2 , Media3 , Media4)

plt.subplot(2,3,6)
barrasMedias = plt.bar(Lojas, Medias, color = 'skyblue')
plt.bar_label(barrasMedias, fmt='R$ %.0f', padding=2, fontsize=10)
plt.ylim(min(Medias) * 0.95, max(Medias) * 1.05)
plt.title('Valor Médio por Venda')

plt.tight_layout()

plt.show()
