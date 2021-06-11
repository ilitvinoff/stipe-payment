from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class ProductModel(models.Model):
    MIN_TOTAL_VALUE, MAX_TOTAL_VALUE, DEFAULT_TOTAL_VALUE = 20, 2000, 100

    uuid = models.UUIDField(models.UUIDField(primary_key=True, default=uuid4, editable=False))
    name = models.CharField(verbose_name=("Coin name"), max_length=255, unique=True, default=uuid4)

    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=("created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=("updated"))
    total_value = models.IntegerField(verbose_name=("Total coin value"), default=DEFAULT_TOTAL_VALUE,
                                      validators=[MaxValueValidator(MAX_TOTAL_VALUE),
                                                  MinValueValidator(MIN_TOTAL_VALUE)])
