import sqlite3
import pandas as pd
import os

# Garante que a pasta exista
os.makedirs('data/processed', exist_ok=True)

# Conecta ao banco
conn = sqlite3.connect('dw/dw_vendas.db')

# Lê a tabela
df = pd.read_sql_query("SELECT * FROM fato_vendas", conn)

# Exporta para CSV
df.to_csv('data/processed/fato_vendas.csv', index=False)

conn.close()
print("✅ Arquivo CSV exportado com sucesso!")




import os
print(os.path.exists('data/raw/vendas.csv'))  # Deve retornar True
