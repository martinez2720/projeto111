import os
import shutil

from_dir= "C://Users//juliamartinez//Downloads"
to_dir= "C://Users//juliamartinez//Imagens"

extensoes_permitidas = ['.txt', '.doc', '.docx', '.pdf']

list_of_files=os.listdir(from_dir)
print(list_of_files)

for arquivo in list_of_files:
    
    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
    caminho_arquivo_origem = os.path.join(from_dir, arquivo)
    caminho_arquivo_destino = os.path.join(to_dir, arquivo)
    shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)

    if not extensao_arquivo:
        continue

    if extensao_arquivo in extensoes_permitidas:
         file_name= os.path.basename(event.src_path)
         path1= from_dir+ '/' + file_name
         path2= to_dir+ '/' + "Arquivos_Documentos"
         path3= to_dir+ '/' + "Arquivos_Documentos" + '/' + file_name
              







os.makedirs(path2)
print("Movendo", arquivo)
shutil.move(path1, path3)