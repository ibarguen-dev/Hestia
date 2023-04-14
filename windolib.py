from time import sleep
from os import chdir, system, path

class Windows():
    def __init__(self):
        pass

    def activadorOffices(self):

        if not path.exists("C:/Program Files/Microsoft Office/Office16"):

            chdir("C:/Program Files (x86)/Microsoft Office/Office16")
            
        
        else:

            chdir("C:/Program Files/Microsoft Office/Office16")
        
        sleep(1)
        
        ativador  = "for /f %x in ('dir /b ..\root\Licenses16\ProPlus2019VL*.xrm-ms') do cscript ospp.vbs /inslic: "'"..\root\Licenses16\%x"'

        system(ativador)
        
        sleep(1)
        
        system("cscript  ospp.vbs /setprt:1688")

        sleep(1)


        system("cscript  ospp.vbs /unpkey:6MWKP >nul")

        sleep(1)

        system("cscript  ospp.vbs /inpkey:NMMKJ-6RK4F-KMJVX-8D9MJ-6MWKP")

        sleep(1)
        
        system("cscript  ospp.vbs /sethst:kms8.msguides.com")

        sleep(1)
        
        system("cscript  ospp.vbs /act")
        
        sleep(1)
        
        print("El office ya esta activado")
        
        sleep(1)
        

    def activadorwindow(self):

        system("winver.exe")

        print(''' 
            Lista de versiones de windows

            1. Windows 10 Pro.
            2. Windows 10 Pro Education.
            3. Windows 10 Pro Education N.
            4. Windows 10 Pro N.
            5. Windows 10 Pro Serial.
            6. Windows 10 Home.
            7. Windows 10 Home Single Language.
            8. Windows 10 Education.
            9. Windows 10 Education N.
            10. Windows 10 Enterprise.
            11. Windows 10 Enterprise G.
            12. Windows 10 Enterprise G N.
            13. Windows 10 Enterprise N
        ''')

        respuesta = input("ingrese el numero de la version de windows 10 que tienes: ")
    
        match  respuesta:
    
            case "1":
            
                system("slmgr /ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J")
            
                system("slmgr /skms kms.digiboy.ir")
            
                system("slmgr /ato")
                


            case "2":
            
                system("slmgr /ipk 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y")
            
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")
            
            case "3":

                system("slmgr /ipk YVWGF-BXNMC-HTQYQ-CPQ99-66QFC")
            
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")


            case "4":

                system("slmgr /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")
            
                respuesta =  "Ingrese 1 si le salio un error sino de enter: "
                    
                system("slmgr /ato")



            case "5":

                system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")


            case "6":

                system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
                
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")


            case "7":
                
                system("slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")
                
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")
        
            case "8":
                
                system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
                
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")

            case "9":

                
                system("slmgr /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")
                
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")

            case "10":
                
                system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")

                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")
        
            case "11":
                
                system("slmgr /ipk YYVX9-NTFWV-6MDM3-9PT4T-4M68B")
                
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")

            case "12":
                
                system("slmgr /ipk 44RPN-FTY23-9VTTB-MP9BX-T84FV")
                
                system("slmgr /skms kms.digiboy.ir")
                
                
                system("slmgr /ato")
        
            case "13":
                
                system("slmgr /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
                
                system("slmgr /skms kms.digiboy.ir")
                
                system("slmgr /ato")