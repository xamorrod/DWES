import requests
import json  
from api_keys import API_KEY  

url = "https://api.nal.usda.gov/fdc/v1/foods/list?api_key=" + API_KEY 

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    
    datos = response.json()  
    
    # Guarda los datos en un archivo JSON
    with open("datos.json", "w") as json_file:
        json.dump(datos, json_file, indent=4)  
    
    print("Datos guardados en 'datos.json'")
else:
    print(f"Error en la solicitud: {response.status_code} - {response.text}")
