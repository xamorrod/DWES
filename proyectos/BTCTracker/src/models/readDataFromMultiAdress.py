import requests
from controllers import remainingTransationsToJSON
from models.getUnconfirmedTransactions import getUnConfirmedTransaction


# Obtenemos las direcciones de las wallets de las transacciones que estan pendientes de confirmación en la Blockchain

def getWalletData():

    try:

        url = "https://blockchain.info/multiaddr?active="
        # Importamos las últimas 10 transacciones pendientes para extraer datos de sus direcciones y analizarlas
        lastDirections = getUnConfirmedTransaction()
        directionsUrl = "|".join(lastDirections)

        # Hacer la solicitud GET a la API
        response = requests.get(url + directionsUrl)
        response.raise_for_status()  

        # Convertir la respuesta en formato JSON
        wallet_data = response.json()

        # Obtener las transacciones
        transactions = wallet_data['txs']

        address = wallet_data.get('addr' , 0) # Dirección
        balance = wallet_data.get('final_balance', 0)  # Balance en satoshis
        tx_count = wallet_data.get('n_tx', 0)  # Número de transacciones
       
        data = {
                "address": address,
                "balance": balance / 1e8,  # Convertir a BTC
                "number_of_transactions": tx_count
            }

        
        
        remainingTransationsToJSON.saveWalletDataToJSON(data)
       

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")

