from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


def validate_positive_non_zero_value(value):
    if value <= 0:
        raise ValidationError('Value should be greater than 0')
