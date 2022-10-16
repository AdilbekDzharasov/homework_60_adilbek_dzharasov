# Generated by Django 4.1.1 on 2022-09-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0007_alter_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('OTHER', 'Other'), ('FURNITURE', 'Furniture'), ('SPORT', 'Sport'), ('COMPUTERS', 'Computer'), ('CLOTHES', 'Clothes'), ('ACCESSORIES', 'Accessories')], default='OTHER', max_length=100, verbose_name='Категория'),
        ),
    ]