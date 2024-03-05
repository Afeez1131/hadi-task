import random
import uuid

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from decimal import Decimal

from bookstore_api.models import Book, Order
from bookstore_api.enums import BookGenre


def create_user(username='testuser', email='test@email.com', password='testpass'):
    return User.objects.create_user(username=username, email=email, password=password)


def generate_isbn(length=14):
    return uuid.uuid4().hex[:length].upper()


def create_book(title='Django for Beginner', author='William S. Vincent', genre=None, isbn=None, price=None):
    if not genre:
        genre = random.choice(BookGenre.values)
    if not isbn:
        isbn = generate_isbn()
    pub_date = timezone.now()
    if not price:
        price = random.randint(1000, 10000)
    return Book.objects.create(title=title, author=author, genre=genre,
                               publication_date=pub_date, isbn=isbn, price=price)


def create_order(book, user, quantity=1):
    return Order.objects.create(book=book, user=user, quantity=quantity)


class BookModelTests(TestCase):
    """Test the book models functionality"""

    def setUp(self):
        self.genre = BookGenre.PROGRAMMING
        self.isbn = generate_isbn()
        self.book = create_book(genre=self.genre, isbn=self.isbn)

    def test_book_str_representation(self):
        book = Book.objects.get(id=1)
        self.assertEqual(str(self.book), f"{book.title} - {book.author} - {book.genre}")

    def test_book_was_created(self):
        book = Book.objects.get(id=1)
        self.assertTrue(Book.objects.filter(id=1).exists())
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(self.book.title, book.title)

    def test_book_genre_is_valid(self):
        self.assertIn(self.genre, BookGenre.values)

    def test_create_book_with_invalid_isbn_length_fails(self):
        with self.assertRaises(ValidationError):
            create_book(isbn=generate_isbn(20))

    def test_create_book_with_invalid_price_fails(self):
        with self.assertRaises(ValidationError):
            create_book(price=-100.50)

    def test_create_book_with_not_unique_isbn_fails(self):
        with self.assertRaises(ValidationError):
            create_book(isbn=self.book.isbn)

    def test_create_book_with_invalid_genre_fails(self):
        with self.assertRaises(ValidationError):
            create_book(genre='Fake Genre')


class OrderTests(TestCase):
    """Test the the functionality of the Order model"""

    def setUp(self):
        self.book = create_book()
        self.user = create_user()
        self.order = create_order(self.book, quantity=2, user=self.user)

    def test_order_str_representation(self):
        self.assertEqual(str(self.order), f'{self.book} - ordered by: {self.user} - {self.order.quantity}')

    def test_book_order_is_created(self):
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(self.order.book, self.book)
        self.assertEqual(self.order.quantity, 2)

    def test_create_order_without_book_fails(self):
        with self.assertRaises(ValidationError):
            Order.objects.create(user=self.user, quantity=3)

    def test_create_order_without_user_fails(self):
        with self.assertRaises(ValidationError):
            Order.objects.create(book=self.book, quantity=5)

    def test_default_quantity_used_if_not_provided(self):
        order = Order.objects.create(book=self.book, user=self.user)
        self.assertEqual(order.quantity, 1)

    def test_order_with_non_existing_book_fails(self):
        with self.assertRaises(ObjectDoesNotExist):
            non_existent_book_id = self.book.id + 10
            order = Order.objects.create(book=Book.objects.get(id=non_existent_book_id), user=self.user)

    def test_negative_quantity_fails(self):
        with self.assertRaises(ValidationError):
            order = Order.objects.create(book=self.book, user=self.user, quantity=0)
