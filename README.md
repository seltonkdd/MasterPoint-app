# MasterPoint App

Um aplicativo mobile desenvolvido em Python e Flet

O propósito desse projeto é ser um Aplicativo frontend de client-side, sendo o frontend do projeto Fullstack MasterPoint que desenvolvi

Backend: (https://github.com/seltonkdd/api-MasterPoint)

# Funcionalidades:

- Uma interface amigável e responsiva para o lado do cliente
- Consumo da API do backend
- Visualização e adição dos pontos
- Visualização da localização atual do usuário

# Pré requisitos

Pra esse frontend ser funcional, o backend deve estar rodando

Python 3.9+

Clone o projeto: https://github.com/seltonkdd/MasterPoint-app

Entre no diretório do projeto

> Faça a instalação das depedências: 
    pip install -r requirements.txt

# Uso

Em `.env` insira a url base da api do sistema

Exemplo:

    BASE_URL='http://localhost:8000/api/v1/'

Ela sera usada como base para os endpoints que a aplicação vai acessar:

`auth/token/`
Para login dos usuários

`clocks/`
Para visualização e registro de seus pontos

`get_maps_image/{latitude}/{longitude}/`
Para salvar a imagem da localização atual e mostrar na interface

#### Para rodar a aplicação, digite no terminal: `flet run`

# Build em APK

É necessário buildar o APK toda vez que você mudar o código fonte, como por exemplo atualizando a `BASE_URL`.

Pra mais informações visite a documentação do [Flet](https://flet.dev/docs/publish)

No terminal, digite `flet build apk`

# Screenshots
![2025-04-28 19-35-22 - frame at 0m1s](https://github.com/user-attachments/assets/daa364cf-9479-4294-ad4b-ee502c494bb7)
![2025-04-28 19-35-22 - frame at 0m20s](https://github.com/user-attachments/assets/796ca9ca-cb29-4e61-9ba2-b921218f3a26)
![2025-04-28 19-35-22 - frame at 0m38s](https://github.com/user-attachments/assets/102adb37-08a3-480f-b8fa-df4364e536be)
