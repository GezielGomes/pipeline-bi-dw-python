import sqlite3
import pandas as pd
import os


# Conecta ao banco
conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'dw_vendas.db'))
cur = conn.cursor()

# Extrai produtos distintos da tabela fato
df_produto = pd.read_sql_query("SELECT DISTINCT produto FROM fato_vendas", conn)

# Cria IDs para a dimensão
df_produto['id_produto'] = range(1, len(df_produto) + 1)

# Reorganiza colunas
df_produto = df_produto[['id_produto', 'produto']]

# Cria a tabela dimensão
cur.execute('''
    CREATE TABLE IF NOT EXISTS dim_produto (
        id_produto INTEGER PRIMARY KEY,
        produto TEXT
    );
''')

# Apaga dados anteriores (opcional)
cur.execute("DELETE FROM dim_produto")

# Insere dados
df_produto.to_sql('dim_produto', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("✅ Tabela dim_produto atualizada com sucesso.")
