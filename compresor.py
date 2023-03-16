from patoolib import extract_archive, create_archive


def Descompresor():
    file = input("Arraste aqui el archivo a descomprimir: ")
    extract_archive(file)

def Compresor():
    file = input("Arraste aqui el archivo a comprimir: ")
    create_archive(file)


def Descomprimir(file):
    extract_archive(file)