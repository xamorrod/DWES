import requests
import json  


url = "https://blockchain.info/unconfirmed-transactions?format=json"

def getUnConfirmedTransaction():
    try:
        
        # Hacer la solicitud GET a la API
        response = requests.get(url)
        response.raise_for_status()  

        # Convertir la respuesta en formato JSON
        data = response.json()

        # Obtener las transacciones
        transactions = data['txs']

        # Obtener las direcciones de las 10 últimas transacciones
        latest_transactions = transactions[:10]
        all_output_addresses = []
        
        for idx, tx in enumerate(latest_transactions):
            print(f"\nTransacción {idx + 1} - Hash: {tx['hash']}")
            
            # Obtener las direcciones de salida (outputs)
            output_addresses = []
            for output in tx['out']:
                # Asegurarse de que la dirección esté presente
                if 'addr' in output:
                    output_addresses.append(output['addr'])
            
            print(f"Direcciones de salida: {', '.join(output_addresses) if output_addresses else 'No disponibles'}")
            all_output_addresses.extend(output_addresses) 

            
        return output_addresses
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las transacciones: {e}")