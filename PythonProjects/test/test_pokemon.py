import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e3815d45683d9922a1a3334a9d57b0ce'
HEADER = {'Conter-type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4973'
TRAINER_NAME = 'Link'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Gooki'

   
   
@pytest.mark.parametrize('key, value', [('name','Gooki'), ('trainer_id', TRAINER_ID), ('id', '65964')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value


def test_name_trainer():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_name' : TRAINER_NAME})
    assert response_get.json()["data"][0]["name"] == 'Link'