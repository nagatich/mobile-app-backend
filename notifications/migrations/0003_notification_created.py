# Generated by Django 3.1.7 on 2021-04-19 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20210418_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]