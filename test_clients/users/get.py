import requests

BASE_URL = 'http://127.0.0.1:8000/api/users/'

response = requests.get(BASE_URL)
json_response = response.json()
print('json response: ', json_response)

"""getting an instance"""
if len(json_response) >= 1:
    print('\n')
    for item in json_response:
        pk = item.get('id')
        url = BASE_URL + str(pk)
        response = requests.get(url)
        print(f'instance with ID: {pk} ', response.json())
