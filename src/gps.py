import flet_geolocator as fg

from services import Client


def get_geolocator():
    gl = fg.Geolocator(
        location_settings=fg.GeolocatorSettings(
            accuracy=fg.GeolocatorPositionAccuracy.BEST
        ))
    return gl

#### FAZER A REQUISIÇÃO PRO SERVIDOR/LOCALHOST E CONSEGUIR A IMAGEM GPS ARMAZENADA NELE
def get_location_image_backend(latitude, longitude):
    client = Client()
    
    endpoint = f'get_maps_image/{latitude}/{longitude}/'
    resposta, status_code = client.get_request(endpoint)

    if status_code == 200:
        with open('assets/imagem_gps.png', "wb") as file:
            file.write(resposta)
