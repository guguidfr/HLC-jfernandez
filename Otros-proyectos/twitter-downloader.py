"""
Es necesario instalar:
    - "requests" => pip install requests
    - "BeautifulSoup" => pip install bs4
    - "urllib3" => pip install urllib3
"""
import requests
from bs4 import BeautifulSoup
import urllib3
# Rellenar el campo del formulario y hacer una solicitud POST
url = 'https://twdown.net/download.php'
tweet = 'https://twitter.com/pincheotaku/status/1618167625787531264'
#data = {'form_field': 'form_value'}
response = requests.post(url, data={'URL':tweet})
# Buscar el elemento y obtener el enlace del href
soup = BeautifulSoup(response.text, 'html.parser')
link = soup.find('td').find('a', href=True)['onclick'] #type: ignore
inicio = link.find("https") # Posición de 'https' #type: ignore
fin = link.find(")") # Posición de ')' #type: ignore
final = link[inicio:fin-1]
ruta = "./"
nombre = "prueba.mp4"
completo = ruta + nombre
#urllib.request.urlretrieve(final, completo)
video = urllib3.PoolManager()
with video.request("GET", final, preload_content=False) as resp, open(completo, "wb") as out_file:
    out_file.write(resp.read())