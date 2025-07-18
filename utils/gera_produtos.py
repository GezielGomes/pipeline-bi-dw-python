import pandas as pd
import random
import os

# Base do script (pasta utils)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Cria a pasta data/raw dentro de utils
raw_dir = os.path.join(base_dir, 'data', 'raw')
os.makedirs(raw_dir, exist_ok=True)

# Caminho do arquivo produtos.csv dentro de utils/data/raw
produtos_path = os.path.join(raw_dir, 'produtos.csv')

categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Brinquedos', 'Livros']
produtos = []

for i in range(1, 1001):
    produto = {
        'id_produto': i,
        'nome_produto': f'Produto {i}',
        'categoria': random.choice(categorias),
        'preco_unitario': round(random.uniform(10.0, 500.0), 2)
    }
    produtos.append(produto)

df = pd.DataFrame(produtos)
df.to_csv(produtos_path, index=False)

print(f"✅ Arquivo produtos.csv gerado com sucesso em {produtos_path}")
