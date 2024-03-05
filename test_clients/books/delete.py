
import requests
import uuid
from datetime import datetime

BASE_URL = 'http://127.0.0.1:8000/api/books/'
all_books = requests.get(BASE_URL).json()
if len(all_books) > 0:
    first = all_books[0]
    delete_url = BASE_URL + f"{str(first.get('id'))}/"
    print('deleting book:', delete_url)
    count = len(requests.get(BASE_URL).json())
    print(f'before delete, we have {count} books')
    response = requests.delete(delete_url)
    count = len(requests.get(BASE_URL).json())
    print(f'after delete, we have {count} books left')
