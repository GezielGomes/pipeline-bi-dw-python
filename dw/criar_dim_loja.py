import os
import sqlite3
import pandas as pd

# Caminho absoluto do arquivo atual (pasta dw)
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'dw_vendas.db')

# Conecta ao banco
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Lê os dados únicos de loja da tabela fato
df = pd.read_sql_query("SELECT DISTINCT loja FROM fato_vendas", conn)

# Cria a tabela dim_loja
cur.execute("""
CREATE TABLE IF NOT EXISTS dim_loja (
    loja TEXT PRIMARY KEY
)
""")
conn.commit()

# Insere os dados únicos na dim_loja
for _, row in df.iterrows():
    cur.execute("""
    INSERT OR IGNORE INTO dim_loja (loja)
    VALUES (?)
    """, (row['loja'],))

conn.commit()
conn.close()

print("✅ Tabela dim_loja criada e populada com sucesso!")



import sqlite3
conn = sqlite3.connect('dw/dw_vendas.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())