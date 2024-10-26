import requests
import json
from readDataFromUnConfirmedTransaction import getUnConfirmedTransaction
from api.apiUrl import INFOTRANS

url = INFOTRANS
lastDirections = getUnConfirmedTransaction()
directionsUrl = "|".join(lastDirections)

# Obtenemos los datos de una transacción dado su Hash 
def getDataFromTransacction(hash):

    try:

        # Hacer la solicitud GET a la API
        response = requests.get(url + addresses)
        response.raise_for_status()

        # Convertir la respuesta en formato JSON
        wallet_data = response.json()

        # Obtener las transacciones
        transactions = wallet_data["txs"]

        balance = wallet_data.get("final_balance", 0)  # Balance en satoshis
        tx_count = wallet_data.get("n_tx", 0)  # Número de transacciones

        # Mostrar los datos
        print(f"Dirección:")
        print(f"Saldo: {balance / 1e8} BTC")  # Convertir de satoshis a BTC
        print(f"Número de transacciones: {tx_count}")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")



