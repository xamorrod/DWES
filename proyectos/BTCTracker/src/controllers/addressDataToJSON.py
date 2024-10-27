from pathlib import Path
import json

# Esta función se encarga de registrar en un JSON los datos de una cuenta cuando se llama a
# la API para obtener estos datos

def saveAllDataToJSON(data):

    # Ruta en la que se va a almacenar
    filename = "./src/data/addresses_data.json"
    file_path = Path(filename)

    try:
        if file_path.exists():
            with open (file_path, "r") as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []
                
        else:
            existing_data = []

        existing_data.append(data)

        # Guardar los datos actualziado en el archivo JSON

        with open(file_path, "w") as file:
            print(f"Datos a guardar: {data}")
            json.dump(existing_data,file, indent =4)

        print(f"Datos guardados en {file_path}")

    except IOError as e:
        print(f"Error al guardar el archivo {filename}: {e}")


