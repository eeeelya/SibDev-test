from django.core.validators import MinValueValidator
from django.db import models


class Gem(models.Model):
    name = models.CharField(default="", max_length=120)


class User(models.Model):
    username = models.CharField(max_length=120, )
    spent_money = models.DecimalField(default=0, decimal_places=0, max_digits=21, validators=[MinValueValidator(0)])
    # gems = models.ForeignKey(Gem, null=True, on_delete=models.PROTECT)
