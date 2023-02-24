# Generated by Django 3.1.7 on 2021-05-08 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_queryresult'),
        ('wish_list', '0002_wishlistitem_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='car_model',
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.brand'),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='generation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.generation'),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.model'),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='modification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.modification'),
        ),
    ]