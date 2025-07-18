import subprocess
import os

scripts = [
    "utils/gera_produtos.py",
    "utils/gera_vendas.py",
    "etl/processa_vendas.py",
    "dw/carrega_dw.py",
    "dw/criar_dim_tempo.py",
    "dw/criar_dim_produto.py",
    "dw/criar_dim_loja.py"
]

print("\n🚀 Iniciando pipeline de atualização do Data Warehouse...\n")

scripts_com_erro = []

for script in scripts:
    print(f"▶️ Executando {script}...")
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Erro ao executar {script}: {e}")
        scripts_com_erro.append(script)

print("\n✅ Pipeline concluído!")

if scripts_com_erro:
    print("⚠️ Scripts com erro:")
    for erro in scripts_com_erro:
        print(f" - {erro}")
else:
    print("🎉 Todos os scripts executados com sucesso!")
