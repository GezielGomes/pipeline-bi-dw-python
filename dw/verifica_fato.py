import sqlite3
import os
import pandas as pd

# Caminho para o banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'dw_vendas.db')

# Conecta ao banco
conn = sqlite3.connect(db_path)

# Lê todos os registros da tabela fato_vendas
df = pd.read_sql_query("SELECT * FROM fato_vendas", conn)

# Exibe as primeiras linhas e o total de registros
print(df.head())
print(f"\nTotal de registros: {len(df)}")

conn.close()
