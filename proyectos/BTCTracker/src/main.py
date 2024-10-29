from models.readDataFromTransaction import getDataFromTransacction



#TODO Corregir entrada de datos en walletData.json ya que al insertarlos usando las direcciones de las transacciones pendientes no se rellenan
#TODO Añadir alguna forma de filtrado o búsqueda de direcciones, carteras o saldo extra
#TODO Implementar interfaz gráfica 
#TODO Implementar contenerización

def main():
    #readDataFromMultiAdress.getWalletData()
    #getUnConfirmedTransaction()
    getDataFromTransacction("3c5bcdcff4e79285e73e3817c717671516cbbd3c10106f8804e900e524aeb6f3")
    
main()