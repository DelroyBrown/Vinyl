# Generated by Django 3.1.4 on 2022-07-05 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_remove_product_funfun'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_address',
        ),
    ]
