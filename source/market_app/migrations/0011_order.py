# Generated by Django 4.1.1 on 2022-10-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0010_productincart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
        ),
    ]
