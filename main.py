from view.view import view
try:
    while True:

        menus = view()
        
        respusta = input("Por favor ingrese una opción de la lista: ")

        match respusta:

            case "1":

                menus.convertidores()

            case "2":

                menus.youtube()

            case "3":

               menus.organaizarArchivos() 

            case "4":

                break
            
            case _:

                print("Error la opción ingresada no existe")

except Exception as e:

    input(e)

    #Hacaer 