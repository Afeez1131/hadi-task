import requests

BASE_URL = 'http://127.0.0.1:8000/api/books/'

resp = requests.get(BASE_URL)
json_response = resp.json()
print('json response: ', json_response)

"""getting an instance"""
if len(json_response) >= 1:
    print('\n\n')
    pk = json_response[0].get('id')
    url = BASE_URL + str(pk)
    response = requests.get(url)
    print(f'instance with ID: {pk} ', response.json())
