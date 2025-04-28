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

Clone o projeto: 

Entre no diretório do projeto

> Faça a instalação das depedências: 
    pip install -r requirements.txt

# Uso

Em `.env` insira a url base da api do sistema

Exemplo:

    BASE_URL='http://localhost:8000/'

Ela sera usada como base para os endpoints que a aplicação vai acessar:

`auth/token/`
Para login dos usuários

`clocks/`
Para visualização e registro de seus pontos

#### Para rodar a aplicação, digite no terminal: `flet run`

# Build em APK

É necessário buildar o APK toda vez que você mudar o código fonte, como por exemplo atualizando a `BASE_URL`.

Pra mais informações visite a documentação do [Flet](https://flet.dev/docs/publish)

No terminal, digite `flet build apk`
