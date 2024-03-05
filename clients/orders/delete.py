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

BASE_URL = 'http://127.0.0.1:8000/api/orders/'
if header:
    orders = requests.get(BASE_URL, headers=header).json().get('results')
    print('orders: ', orders)
    if len(orders) > 0:
        last = orders[-1]
        delete_url = BASE_URL + f"{last.get('id')}/"
        print('deleting order:', delete_url)
        count = len(requests.get(BASE_URL, headers=header).json().get('results'))
        print(f'before delete, we have {count} orders')
        response = requests.delete(delete_url, headers=header)
        count = len(requests.get(BASE_URL, headers=header).json().get('results'))
        print(f'after delete, we have {count} orders left')
else:
    print(f'authentication header not provided {header}')
