import requests

AUTH_URL = 'http://127.0.0.1:8000/api/token-auth'
auth_data = {'username': 'admin', 'password': 'password',}

response = requests.post(AUTH_URL, data=auth_data)
json_response = response.json()
if response.status_code != 200:
    header = {}
else:
    token = json_response.get('token')
    header = {'Authorization': 'Token ' + token}

BASE_URL = 'http://127.0.0.1:8000/api/books/'
if header:
    resp = requests.get(BASE_URL, headers=header)
    json_response = resp.json()
    print('json response: ', json_response)

    """getting an instance"""
    if len(json_response) >= 1:
        print('\n\n')
        pk = json_response.get('results')[0].get('id', '')
        url = BASE_URL + str(pk)
        response = requests.get(url, headers=header)
        print(f'instance with ID: {pk} ', response.json())
else:
    print(f'invalid authentication header {header}')
