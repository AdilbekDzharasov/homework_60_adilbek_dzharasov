# Generated by Django 4.1.1 on 2022-09-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость'),
        ),
    ]
