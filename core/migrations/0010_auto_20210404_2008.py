# Generated by Django 3.1.7 on 2021-04-04 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_brand_generation_model_modification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generation',
            name='production_from',
        ),
        migrations.RemoveField(
            model_name='generation',
            name='production_to',
        ),
        migrations.RemoveField(
            model_name='modification',
            name='power_range_from',
        ),
        migrations.RemoveField(
            model_name='modification',
            name='power_range_to',
        ),
    ]