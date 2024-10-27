import requests
import json
from controllers import balanceToJSON
from pathlib import Path


# Obtenemos los datos de una transacción dado su Hash
def getBalanceFromAddress(address):

    url = "https://blockchain.info/balance?active="

    try:

        # Hacer la solicitud GET a la API
        response = requests.get(url + address)
        response.raise_for_status()

        # Convertir la respuesta en formato JSON
        wallet_data = response.json()

        # Acceder a los datos de la dirección proporcionada
        address_data = wallet_data.get(address, {})

        # Obtener las transacciones

        balance = address_data.get("final_balance", 0)  # Balance en satoshis
        total_receive = address_data.get("total_received", 0)
        n_tx = address_data.get("n_tx", 0)  # Total recibido

        # Crear un diccionario con los datos obtenidos
        data = {
            "address": address,
            "balance": balance / 1e8,
            "total_received": total_receive / 1e8,
            "number_of_transactions": n_tx
        }
        balanceToJSON.saveBalanceToJSON(data)
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")
