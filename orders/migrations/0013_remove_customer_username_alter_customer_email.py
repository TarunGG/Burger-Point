# Generated by Django 4.1.5 on 2023-03-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
