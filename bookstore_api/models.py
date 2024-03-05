from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from .enums import BookGenre
from .validators import validate_positive_non_zero_value


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=155)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=14, unique=True)
    genre = models.CharField(max_length=55, choices=BookGenre.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive_non_zero_value])
    quantity = models.PositiveIntegerField(default=1, validators=[validate_positive_non_zero_value])

    class Meta:
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.genre}"


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[validate_positive_non_zero_value])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book} - ordered by: {self.user} - {self.quantity}"
