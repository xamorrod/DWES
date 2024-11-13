from bannerApp import imprimirBanner
import models
import models.getUnconfirmedTransactions

# Implementamos el método que va a ser el menu de la app encargado de 
# conectar el menu principal con las funciones de conexión a los datos

def menuUtil():
    
    # Inicializamos las variables necesarias 
    confirm = False
    imprimirBanner()
    print("Bienvenido a la aplicación BTC Tracker, orientada a rastrear datos de la BlockChain")
    
    while(not confirm): 
        
        option = input(print("Introduce la opción según la opción que desees\n1- Consultar las transacciones pendientes de la red de BTC\n2- Consultar el balance dada una dirección de BTC\n3- Consultar los datos de una Wallet\n4- Obtener los datos dada una transacción"))
        
        match option:
            case 1:
                #Transacciones pendientes en la red de BTC
                models.getUnconfirmedTransactions.getUnConfirmedTransaction()

                break
            case 2:
                
                break
            case 3:
                
                break
            case 4:
                
                break
            
        
menuUtil()       