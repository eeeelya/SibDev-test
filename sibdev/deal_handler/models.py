from django.core.validators import MinValueValidator
from django.db import models


class Deal(models.Model):
    customer = models.CharField(default="", max_length=120)
    item = models.CharField(default="", max_length=120)
    total = models.FloatField(default=0, validators=[MinValueValidator(0)])
    quantity = models.FloatField(default=0, validators=[MinValueValidator(0)])
    date = models.DateTimeField(auto_now_add=True)
