from django.db import models


class BookGenre(models.TextChoices):
    FICTION = 'Fiction'
    NON_FICTION = 'Non-Fiction'
    MYSTERY = 'Mystery'
    ROMANCE = 'Romance'
    SCIENCE_FICTION = 'Science Fiction'
    HORROR = 'Horror'
    THRILLER = 'Thriller'
    FANTASY = 'Fantasy'
    BIOGRAPHY = 'Biography'
    HISTORY = 'History'
    SELF_HELP = 'Self-Help'
    POETRY = 'Poetry'
    DRAMA = 'Drama'
    COMICS = 'Comics'
    COOKBOOK = 'Cookbook'
    TRAVEL = 'Travel'
    CHILDREN = 'Children'
    YOUNG_ADULT = 'Young Adult'
    PROGRAMMING = 'Programming'
