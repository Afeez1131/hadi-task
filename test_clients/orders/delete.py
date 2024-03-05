import requests

BASE_URL = 'http://127.0.0.1:8000/api/orders/'
orders = requests.get(BASE_URL).json()
if len(orders) > 0:
    last = orders[-1]
    delete_url = BASE_URL + f"{last.get('id')}/"
    print('deleting order:', delete_url)
    count = len(requests.get(BASE_URL).json())
    print(f'before delete, we have {count} orders')
    response = requests.delete(delete_url)
    count = len(requests.get(BASE_URL).json())
    print(f'after delete, we have {count} orders left')
