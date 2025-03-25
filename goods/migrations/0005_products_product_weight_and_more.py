# Generated by Django 5.1.7 on 2025-03-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_products_type_of_personality'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_weight',
            field=models.TextField(blank=True, null=True, verbose_name='Вес товара'),
        ),
        migrations.AddField(
            model_name='products',
            name='pyramid_of_fragrance',
            field=models.TextField(blank=True, null=True, verbose_name='Пирамида аромата'),
        ),
        migrations.AddField(
            model_name='products',
            name='type_product',
            field=models.TextField(blank=True, null=True, verbose_name='Тип продукта'),
        ),
    ]
