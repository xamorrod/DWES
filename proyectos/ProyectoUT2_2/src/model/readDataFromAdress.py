import requests
from readUnConfirmedTransaction import getUnConfirmedTransaction

address = "bc1qu59a5y5qm9cv68r9gxa3g0vduckpp9zxry4a2a"

url = "https://blockchain.info/rawaddr/" + address

#Importamos las últimas 10 transacciones pendientes para extraer datos de sus direcciones y analizarlas

lastDirections = getUnConfirmedTransaction()

def getWalletData(address):
    
    try:
        
        # Hacer la solicitud GET a la API
        response = requests.get(url)
        response.raise_for_status()  

        # Convertir la respuesta en formato JSON
        wallet_data = response.json()

        # Obtener las transacciones
        transactions = wallet_data['txs']

        balance = wallet_data.get('final_balance', 0)  # Balance en satoshis
        tx_count = wallet_data.get('n_tx', 0)  # Número de transacciones

        # Mostrar los datos
        print(f"Dirección: {address}")
        print(f"Saldo: {balance / 1e8} BTC")  # Convertir de satoshis a BTC
        print(f"Número de transacciones: {tx_count}")
        
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")
    

getWalletData(address)

for address in lastDirections :
    url = "https://blockchain.info/rawaddr/"
    
    