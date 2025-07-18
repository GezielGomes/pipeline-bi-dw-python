import sqlite3
import pandas as pd
import os

# Conecta ao banco
conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'dw_vendas.db'))

cur = conn.cursor()

# Lê todas as datas distintas da tabela fato_vendas
df = pd.read_sql_query("SELECT DISTINCT data FROM fato_vendas", conn)

# Garante que as datas estejam no formato datetime
df['data'] = pd.to_datetime(df['data'])

# Cria as colunas da dimensão tempo
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df['dia'] = df['data'].dt.day
df['trimestre'] = df['data'].dt.quarter
df['dia_semana'] = df['data'].dt.day_name()

# Cria a tabela dim_tempo
cur.execute("""
CREATE TABLE IF NOT EXISTS dim_tempo (
    data DATE PRIMARY KEY,
    ano INTEGER,
    mes INTEGER,
    dia INTEGER,
    trimestre INTEGER,
    dia_semana TEXT
)
""")

conn.commit()

# Insere os dados na dim_tempo
for _, row in df.iterrows():
    cur.execute("""
    INSERT OR IGNORE INTO dim_tempo (data, ano, mes, dia, trimestre, dia_semana)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (row['data'].date(), row['ano'], row['mes'], row['dia'], row['trimestre'], row['dia_semana']))

conn.commit()
conn.close()

print("✅ Tabela dim_tempo criada e populada com sucesso!")
