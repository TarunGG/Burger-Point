# Generated by Django 4.1.5 on 2023-02-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_menu_orders_delete_burger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
