import pandas as pd
import os

# Caminho base: a pasta onde o script está
base_path = os.path.dirname(os.path.abspath(__file__))

# Caminhos corretos relativos à raiz do projeto
raw_path = os.path.join(base_path, '../data/raw/vendas.csv')
processed_path = os.path.join(base_path, '../data/processed/vendas_tratada.csv')

# Leitura do CSV
df = pd.read_csv(raw_path)

# Transformação
df.columns = [col.lower() for col in df.columns]
df['data'] = pd.to_datetime(df['data'])
df['total_venda'] = df['quantidade'] * df['preco_unitario']

# Garante que a pasta processed exista
os.makedirs(os.path.dirname(processed_path), exist_ok=True)

# Salva o resultado
df.to_csv(processed_path, index=False)

print(f"ETL finalizado! Arquivo salvo em: {processed_path}")




