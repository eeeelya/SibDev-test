# Generated by Django 4.2.5 on 2023-09-04 21:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal_handler', '0002_gem_user_delete_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='spent_money',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=21, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
