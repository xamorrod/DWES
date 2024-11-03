from views.bannerApp import imprimirBanner
from models import readDataFromAddress
from models import readDataFromTransaction


#TODO Añadir alguna forma de filtrado o búsqueda de direcciones, carteras o saldo extra
#TODO Implementar interfaz gráfica 
#TODO Implementar contenerización

def main():
    #readDataFromMultiAdress.getWalletData()
    #getUnConfirmedTransaction()
    #getDataFromTransacction("3c5bcdcff4e79285e73e3817c717671516cbbd3c10106f8804e900e524aeb6f3")
    readDataFromTransaction.getDataFromTransacction("435d77b74b328dc8dd62c27d5ebae9dc92d56128a1acdf44ac6fb705cbbbc0ec")
    readDataFromAddress.getDataFromAddress("bc1q0fm8dvvqr6jpfagtycjx3guknazta2qeul7luz")

main()