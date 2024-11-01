import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6f509b770421bcea67816e866f23792e'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '7446'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200


def test_traiter_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Фидель'

   
   
