# Generated by Django 3.1.7 on 2021-03-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_car_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
