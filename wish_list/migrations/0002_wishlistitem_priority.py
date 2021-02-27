# Generated by Django 3.1.7 on 2021-02-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistitem',
            name='priority',
            field=models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=1),
        ),
    ]