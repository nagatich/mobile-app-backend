# Generated by Django 3.1.7 on 2021-04-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='text',
            new_name='message',
        ),
        migrations.AddField(
            model_name='notification',
            name='event',
            field=models.CharField(default='notification', max_length=200, verbose_name='Событие'),
        ),
    ]
