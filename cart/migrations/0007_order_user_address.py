# Generated by Django 3.1.4 on 2021-01-10 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20210101_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.address'),
        ),
    ]
