# Generated by Django 4.1.5 on 2023-02-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='pin',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default=None, max_length=100),
        ),
    ]