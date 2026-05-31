import os
import shutil

caminho_documentos = "C:/Users/mimim/OneDrive/Documentos"

mapeamento = {
    ".pdf": "Documentos_PDF",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".jpeg": "Imagens",
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".mp4": "Vídeos",
    ".mp3": "Músicas",
    ".txt": "Textos",
}

def organizar_pasta():
    print("--- Iniciando a faxina automática ---")

    # 1. Garante que a pasta existe
    if not os.path.exists(caminho_documentos):
        print("Caminho não encontrado.")
        return
    
    # 2. Olha tudo que tem dentro da pasta
    arquivos = os.listdir(caminho_documentos)

    for item in arquivos:
        # AQUI FOI CORRIGIDO: Juntando o caminho da pasta com o nome do arquivo
        caminho_completo_item = os.path.join(caminho_documentos, item)

        # Ignora pastas, só organiza arquivos
        if os.path.isdir(caminho_completo_item):
            continue

        # 3. Pega a extensão do arquivo
        nome_arquivo, extensao = os.path.splitext(item)
        extensao = extensao.lower() # Garante que funciona mesmo se for .JPG maiúsculo

        # 4. Se a extensão estiver no mapeamento, move o arquivo
        if extensao in mapeamento:
            nome_pasta_destino = mapeamento[extensao]
            caminho_pasta_destino = os.path.join(caminho_documentos, nome_pasta_destino)

            # Se a pasta destino não existir, cria ela
            if not os.path.exists(caminho_pasta_destino):
                os.makedirs(caminho_pasta_destino)
                print(f"Pasta {nome_pasta_destino} criada.")

            # Move o arquivo para a pasta destino
            shutil.move(caminho_completo_item, os.path.join(caminho_pasta_destino, item))
            print(f"Arquivo {item} movido para a pasta {nome_pasta_destino}.")

    print("--- Faxina automática concluída ---")

if __name__ == "__main__":
    organizar_pasta()