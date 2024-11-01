import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6f509b770421bcea67816e866f23792e'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_registration = {
  "name": "СтраусМурзик",
  "photo_id": 89
}

body_change = {
    "pokemon_id": "121416",
    "name": "Дед Максим",
    "photo_id": 560
}

body_kip_pockeball = {
    "pokemon_id": "121416"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(response_create.text)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change_name.text)

response_kip_pockeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_change)
print(response_kip_pockeball.text)
