import requests
from controllers import addressDataToJSON



# Obtenemos las direcciones de las wallets de las transacciones que estan pendientes de confirmación en la Blockchain

def getDataFromAddress(address):

    try:

        url = "https://blockchain.info/rawaddr/"
        
        # Hacer la solicitud GET a la API
        response = requests.get(url + address)
        response.raise_for_status()  

        # Convertir la respuesta en formato JSON
        wallet_data = response.json()

        # Acceder a los datos de la dirección proporcionada
        address_data = wallet_data.get(address, {})

        address = wallet_data.get('address' , 0) # Dirección
        balance = wallet_data.get('final_balance', 0)  # Balance en satoshis
        total_received = wallet_data.get('total_received', 0)
        total_sent = wallet_data.get('total_sent', 0)
        tx_count = wallet_data.get('n_tx', 0)  # Número de transacciones
        
        data = {
            "address": address,
            "balance": balance / 1e8,
            "total_received": total_received / 1e8,
            "total_sent" : total_received / 1e8,
            "number_of_transactions": tx_count
        }
        addressDataToJSON.saveAllDataToJSON(data)
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")

