import os

# Caminho padrão do Windows para a pasta Documentos
# Mudei o caminho para incluir o OneDrive do sistema!
caminho_documentos = "C:/Users/mimim/OneDrive/Documentos"

def testar_pasta():
    print("--- INICIANDO DIAGNÓSTICO ---")
    
    # 1. Verifica se a pasta existe de verdade no seu PC
    if os.path.exists(caminho_documentos):
        print(f"✅ Sucesso: O Python achou a pasta: {caminho_documentos}")
    else:
        print(f"❌ Erro: O Python NÃO achou essa pasta. O caminho está errado!")
        return

    # 2. Tenta listar o que tem dentro
    arquivos = os.listdir(caminho_documentos)
    
    print(f"Quantidade de arquivos encontrados lá dentro: {len(arquivos)}")
    
    print("--- Arquivos encontrados: ---")
    for item in arquivos:
        print(f"- {item}")
    print("-----------------------------")

if __name__ == "__main__":
    testar_pasta()