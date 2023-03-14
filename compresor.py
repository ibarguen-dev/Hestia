from patoolib import extract_archive, create_archive


class Descompresor:
    file = input("Arraste aqui el archivo a descomprimir: ")
    extract_archive(file)

class Compresor:
    file = input("Arraste aqui el archivo a comprimir: ")
    create_archive(file)

class DescompresorHestia:
    def Descomprimir(file):
        extract_archive(file)