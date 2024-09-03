import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e3815d45683d9922a1a3334a9d57b0ce'
HEADER = {'Conter-type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "krestovskii.k@yandex.ru",
    "password": "Iloveqa1111"
}


response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)