from view.view import view
try:
    while True:

        menus = view()
        
        respusta = input("Porfavor ingrese una opcionde la lista del menu: ")

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

                print("Error la opcion ingresada no existe")

except Exception as e:

    input(e)