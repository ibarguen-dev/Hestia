from automatizador import windows
from config import menu, convertidores, compresore,youtube
from os import system








while True:
    try:
        windows()
        menu()
        respuesta = input("Ingrese un una opcion del menu: ")
        match respuesta:
            case "1":
                convertidores()
            case "2":
                compresore()
            case "3":
                youtube()
            case "4":
                break
            case _:
                print("La opcion ingresada no existe")
            
        system("cls")

    except Exception as e:
        print(e)
