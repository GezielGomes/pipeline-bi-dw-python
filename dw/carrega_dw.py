import pandas as pd
import sqlite3
import os

# Caminho do banco de dados
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'dw_vendas.db')

# Caminho do CSV tratado
csv_path = os.path.join(base_dir, '..', 'data', 'processed', 'vendas_tratada.csv')

# Carrega o CSV
df = pd.read_csv(csv_path)

# Conecta ao banco
conn = sqlite3.connect(db_path)

# Substitui a tabela fato_vendas com os dados atuais do CSV
df.to_sql('fato_vendas', conn, if_exists='replace', index=False)

conn.close()

print("✅ Carga de dados concluída com sucesso!")


