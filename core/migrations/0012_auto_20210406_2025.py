# Generated by Django 3.1.7 on 2021-04-06 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210404_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='generation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.generation'),
        ),
    ]
