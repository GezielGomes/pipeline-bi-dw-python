import os
import pandas as pd
import random
from datetime import datetime, timedelta

# Caminho correto (relativo à raiz do projeto)
base_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.abspath(os.path.join(base_path, '..', 'data', 'raw', 'vendas.csv'))

# Simula dados
produtos = [f"Produto {i}" for i in range(1000)]
categorias = ["Eletrônicos", "Livros", "Roupas", "Alimentos", "Brinquedos"]
lojas = ["Loja A", "Loja B", "Loja C", "Loja D", "Loja E"]

dados = []

for _ in range(10000):
    produto = random.choice(produtos)
    categoria = random.choice(categorias)
    data = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 545))
    quantidade = random.randint(1, 10)
    preco_unitario = round(random.uniform(10, 5000), 2)
    loja = random.choice(lojas)
    dados.append([data.strftime('%Y-%m-%d'), produto, categoria, quantidade, preco_unitario, loja])

df = pd.DataFrame(dados, columns=["data", "produto", "categoria", "quantidade", "preco_unitario", "loja"])

# Garante que a pasta exista
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"✅ Arquivo vendas.csv gerado com {len(df)} registros em: {output_path}")
