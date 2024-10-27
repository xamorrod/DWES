from pathlib import Path
import json

# Esta función se encarga de registrar en un JSON los datos de balance de una cuenta cuando se llama a
# la API para obtener estos datos

def saveBalanceToJSON(data ,  filename = "addresses_balance.json"):

    # Ruta en la que se va a almacenar

    file_path = Path(filename)

    try:
        if file_path.exists():
            with open (file_path, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        existing_data.append(data)

        # Guardar los datos actualziado en el archivo JSON

        with open(file_path, "w") as file:
            json.dump(existing_data,file, ident =4)

        print("Datos guardados en {file_path}")

    except IOError as e:
        print(f"Error al guardar el archivo {filename}: {e}")


