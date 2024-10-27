import requests
import json
from readDataFromUnConfirmedTransaction import getUnConfirmedTransaction


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
        total_receive = address_data.get("total_received", 0)  # Total recibido

        # Mostrar los datos
        print(f"Dirección:")
        print(f"Saldo: {balance / 1e8} BTC")  # Convertir de satoshis a BTC
        print(f"Total recibido: {total_receive / 1e8} BTC")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")

getBalanceFromAddress("bc1q0qfzuge7vr5s2xkczrjkccmxemlyyn8mhx298v")
