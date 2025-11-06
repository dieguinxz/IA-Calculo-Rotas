import os
import shutil

def limpar_cache(caminho='.'):
    removidos = 0
    for root, dirs, files in os.walk(caminho):
        # Copiamos a lista pois vamos modificar dirs durante o loop
        for dir_name in list(dirs):
            if dir_name in ("__pycache__", "cache"):
                caminho_dir = os.path.join(root, dir_name)
                shutil.rmtree(caminho_dir, ignore_errors=True)
                print(f"Removido diretório: {caminho_dir}")
                removidos += 1

        # Apagar arquivos .pyc e .pyo
        for file_name in files:
            if file_name.endswith(('.pyc', '.pyo')):
                caminho_arq = os.path.join(root, file_name)
                os.remove(caminho_arq)
                print(f" Removido arquivo: {caminho_arq}")
                removidos += 1

    if removidos == 0:
        print(" Nenhum cache encontrado.")
    else:
        print(f"\n Limpeza concluída! {removidos} itens removidos.")

if __name__ == "__main__":
    limpar_cache(".")