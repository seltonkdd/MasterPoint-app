import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Client:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.session = requests.Session()
        self.token = None

    def get_request(self, endpoint: str):
        try:
            if self.token:
                self.session.headers.update({"Authorization": f"Bearer {self.token}"})

            if not self.base_url:
                return 'BASE URL não fornecida'
            
            response = self.session.get(self.base_url + endpoint)
            status_code = response.status_code
            if 'application/json' in response.headers.get('Content-Type', ''):
                result = response.json()
            else:
                result = response.content
            return result, status_code
        except requests.exceptions.ConnectionError:
            return 'Erro ao conectar', None

    def post_request(self, endpoint: str, data: dict):
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

        try:
            if not self.base_url:
                return 'BASE URL não fornecida'

            response = self.get_request(self.base_url + endpoint)
            csrf_token = self.session.cookies.get('csrftoken')

            self.session.headers.update({'X-CSRFToken': csrf_token})

            response = self.session.post(self.base_url + endpoint, json=data)

            result = response.json()
            status_code = response.status_code
            if 'access' in result:
                self.token = result['access']
            if status_code == 200:
                return None
            elif status_code == 201:
                return None
            else:
                return result['detail']
        except requests.exceptions.ConnectionError:
            return 'Erro ao conectar'
