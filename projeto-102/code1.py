import os 
import shutil

items = os.getcwd()

lista = os.listdir(items)
print(lista)

pasta2 = os.getcwd()+"\pasta2"

documentos = os.getcwd()+"\documentos"
for arquivo in lista:
    nome, extensao = os.path.splitext(arquivo)
    if extensao in [".pdf"]:
        os.makedirs(documentos)
    
    shutil.move(pasta2, documentos)
