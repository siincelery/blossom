# Generated by Django 5.1.7 on 2025-03-25 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_products_product_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Скидка в %'),
        ),
    ]
