from pathlib import Path
import json

# Esta función se encarga de guardar los datos de las wallets en un archivo JSON

def saveWalletDataToJSON(data):

    # Ruta en la que se va a almacenar
    filename = "./src/data/wallets_data.json"
    file_path = Path(filename)

    try:
        if file_path.exists():
            with open(file_path, "r") as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        # Crear un nuevo registro con los datos de la wallet
        existing_data.append(data)

        # Guardar los datos actualizados en el archivo JSON
        with open(file_path, "w") as file:
            json.dump(existing_data, file, indent=4)

        

        print(f"Datos de wallet guardados en {file_path}")

    except IOError as e:
        print(f"Error al guardar el archivo {filename}: {e}")