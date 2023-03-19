from automatizador import windows
from config import menu
from config import convertidores









while True:
    try:
        windows()
        menu()
        respuesta = input("Ingrese un una opcion del menu: ")
        match respuesta:
            case "1":
                convertidores()
            case "2":
                
            case "3":
            
            case "5":
                break
            case _:
                print("La opncion ingresada no existe")
            

    except Exception as e:
        print(e)





