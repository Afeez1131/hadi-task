import uuid
from datetime import datetime
from decimal import Decimal

import requests
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from .test_models import create_book, create_user

from bookstore_api.models import Book

BOOKS_URL = 'http://localhost:8000/api/books/'
BOOK_INSTANCE_URL = BOOKS_URL + '1/'
AUTH_URL = 'http://127.0.0.1:8000/api/token-auth'


def get_book_data():
    return {
        'title': 'Django for Dummy',
        'author': 'William S. Vincent',
        'publication_date': datetime.now().date(),
        'isbn': uuid.uuid4().hex[:14].upper(),
        'genre': 'Programming',
        'price': Decimal(134.50)
    }


def get_auth_headers(token):
    return {'Authorization': 'Token ' + token}


class BookApiTest(TestCase):
    """Test case for the Book API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.isbn = uuid.uuid4().hex[:14].upper()
        self.book = create_book(isbn=self.isbn)
        auth_data = {
            'username': 'admin',
            'password': 'password',
            'email': 'admin@gmail.com'
        }
        self.user = create_user(**auth_data)
        token, _ = Token.objects.get_or_create(user=self.user)
        self.headers = get_auth_headers(token.key)
        self.book_data = get_book_data()

    def test_book_not_created_without_auth_header(self):
        data = self.book_data
        response = self.client.post(BOOKS_URL, data=data)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_book_not_created_without_valid_auth_header(self):
        headers = {'Authorization': 'Token 12345678'}
        response = self.client.post(BOOKS_URL, data=self.book_data, headers=headers)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'detail': 'Invalid token.'})

    def test_create_book(self):
        data = get_book_data()
        response = self.client.post(BOOKS_URL, data=data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        all_response = self.client.get(BOOKS_URL).json().get('results')
        self.assertEqual(len(all_response), 2)

    def test_get_all_books_without_headers(self):
        response = self.client.get(BOOKS_URL)
        self.assertEqual(response.status_code, 200)

    def test_get_all_books_with_headers(self):
        response = self.client.get(BOOKS_URL, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_not_created_without_unique_isbn(self):
        data = get_book_data()
        data.update({'isbn': self.isbn})
        response = self.client.post(BOOKS_URL, data=data, headers=self.headers)
        self.assertListEqual(['book with this isbn already exists.'], response.json().get('isbn'))
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_not_created_with_invalid_genre(self):
        data = get_book_data().update({'genre': 'Invalid Genre'})
        response = self.client.post(BOOKS_URL, data=data, headers=self.headers)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_not_created_with_invalid_price(self):
        data = get_book_data()
        data.update({'price': Decimal(-1450.50)})
        response = self.client.post(BOOKS_URL, data=data, headers=self.headers)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertListEqual(['Value should be greater than 0'], response.json().get('price'))


class BookInstanceApiTest(TestCase):
    """Test case for the Book Instance API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.isbn = uuid.uuid4().hex[:14].upper()
        self.book = create_book(isbn=self.isbn)
        auth_data = {
            'username': 'admin',
            'password': 'password',
            'email': 'admin@gmail.com'
        }
        self.user = create_user(**auth_data)
        token, _ = Token.objects.get_or_create(user=self.user)
        self.headers = get_auth_headers(token.key)
        self.book_data = get_book_data()

    def test_get_book_instance_without_auth_header_fail(self):
        response = self.client.get(BOOK_INSTANCE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_instance_with_auth_header(self):
        response = self.client.get(BOOK_INSTANCE_URL, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_instance_full_update_with_valid_header(self):
        book_data = get_book_data()
        book_data.update({
            'title': 'Updated title',
            'author': 'Vincent S.',
            'publication_date': datetime.now().date(),
            'isbn': uuid.uuid4().hex[:14].upper(),
            'genre': 'Fiction',
            'price': Decimal(1250.50)
        })
        response = self.client.put(BOOK_INSTANCE_URL, data=book_data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_instance_full_update_without_valid_header_fail(self):
        book_data = get_book_data()
        book_data.update({
            'title': 'Updated title',
            'author': 'Vincent S.',
            'publication_date': datetime.now().date(),
            'isbn': uuid.uuid4().hex[:14].upper(),
            'genre': 'Fiction',
            'price': Decimal(1250.50)
        })
        response = self.client.put(BOOK_INSTANCE_URL, data=book_data, headers={'Authorization': 'Token Invalid token'})
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book_instance(self):
        response = self.client.delete(BOOK_INSTANCE_URL, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_instance_without_valid_auth_header_fail(self):
        response = self.client.delete(BOOK_INSTANCE_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_partial_update_not_supported(self):
        data = {'title': 'Updated TItle (latest)',
                'author': 'John Doe'}
        response = self.client.patch(BOOK_INSTANCE_URL, data=data, headers=self.headers)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
