import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_urls_with_login(login_url, main_page_url, username, password):
    with requests.Session() as session:
        # Configura el User-Agent para que parezca una solicitud de navegador
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        # Realiza una solicitud GET inicial para obtener el formulario de inicio de sesión
        initial_response = session.get(login_url, headers=headers)
        initial_soup = BeautifulSoup(initial_response.text, "html.parser")

        # Si hay un token CSRF, inclúyelo en el formulario de datos
        csrf_token = initial_soup.find("input", {"name": "csrf_token"})
        csrf_token_value = csrf_token["value"] if csrf_token else None

        # Datos para el inicio de sesión
        login_data = {"username": username, "password": password}
        if csrf_token_value:
            login_data["csrf_token"] = csrf_token_value

        # Realiza la solicitud POST para iniciar sesión
        login_response = session.post(login_url, data=login_data, headers=headers)

       

        # Ahora que estamos logueados, accedemos a la página principal
        response = session.get(main_page_url, headers=headers)
        if response.status_code != 200:
            print(f"Error al acceder a la página principal: {response.status_code}")
            return set()

        # Analiza el contenido HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Encuentra todas las etiquetas <a> y extrae los enlaces
        urls = set()
        for link in soup.find_all("a", href=True):
            # Construye la URL completa
            full_url = urljoin(main_page_url, link["href"])
            urls.add(full_url)

        return urls


# Ejemplo de uso
login_page = (
    "https://www.privilegiosencompras.es/"  # URL de la página de inicio de sesión
)
main_page = "https://www.privilegiosencompras.es/Benefits/Earnings"  # URL de la página principal después de iniciar sesión
username = "galvez09bernardo@tutamail.com"
password = "BerTGal3."


urls = extract_urls_with_login(login_page, main_page, username, password)
for url in urls:
    print(url)
