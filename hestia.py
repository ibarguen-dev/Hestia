import view
try:
    while True:

        menus = view.menu()
        
        respusta = input("Porfavor ingrese una opcionde la lista del menu: ")

        match respusta:

            case "1":

                menus.convertidores()

            case "2":

                menus.compresore()

            case "3":

                menus.youtube()

            case "4":

                menus.clean()

            case "5":

                menus.windowslib()
            
            case "6":

                break
            case _:

                print("Error la opcion ingresada no existe")

except Exception as e:

    input(e)