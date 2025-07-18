import sqlite3
import os

# Garante que a pasta 'dw' existe
os.makedirs('dw', exist_ok=True)

# Cria (ou conecta) o banco SQLite
conn = sqlite3.connect('dw/dw_vendas.db')  # cria o arquivo se não existir

# Cria um cursor (permite executar comandos SQL)
cur = conn.cursor()

# Criação da tabela fato (se ainda não existir)
cur.execute("""
CREATE TABLE IF NOT EXISTS fato_vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE,
    produto TEXT,
    categoria TEXT,
    quantidade INTEGER,
    preco_unitario REAL,
    loja TEXT,
    total_venda REAL
)
""")

# Salva as alterações no banco
conn.commit()

# Fecha a conexão
conn.close()

print("✅ Data Warehouse criado com sucesso!")
