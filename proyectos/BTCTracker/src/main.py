from models.readDataFromMultiAdress import getWalletData


#TODO Corregir entrada de datos en walletData.json ya que al insertarlos usando las direcciones de las transacciones pendientes no se rellenan
#TODO Añadir alguna forma de filtrado o búsqueda de direcciones, carteras o saldo extra
#TODO Implementar interfaz gráfica 
#TODO Implementar contenerización

def main():
    #readDataFromMultiAdress.getWalletData()
    getWalletData()

main()