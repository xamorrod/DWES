import requests
from datetime import datetime
from controllers import transactionDataToJSON


# Obtenemos los datos de una transacción dado su Hash
def getDataFromTransacction(hash):

    url = "https://blockchain.info/rawtx/"
   

    try:

        # Hacer la solicitud GET a la API
        response = requests.get(url + hash)
        response.raise_for_status()

        # Convertir la respuesta en formato JSON
        transaction_data = response.json()

        # Obtener la fecha y hora en formato legible
        timestamp = transaction_data.get("time", 0)
        date_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Crear un diccionario con los datos relevantes
        data = {
            
        "transaction_hash": transaction_data.get("hash"),
        "date_time": date_time,
        "total_fee": transaction_data.get("fee", 0) / 1e8,  # en BTC
        "inputs": [
            {
                "sender_address": input_data["prev_out"].get("addr", "N/A"),
                "amount_sent": input_data["prev_out"].get("value", 0) / 1e8  # en BTC
            }
            for input_data in transaction_data.get("inputs", [])
        ],
        "outputs": [
            {
                "receiver_address": output_data.get("addr", "N/A"),
                "amount_received": output_data.get("value", 0) / 1e8  # en BTC
            }
            for output_data in transaction_data.get("out", [])
        ]
    }
        
        transactionDataToJSON.saveTransactionDataToJSON(data)

        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")
