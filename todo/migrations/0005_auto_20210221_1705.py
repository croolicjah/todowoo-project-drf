# Generated by Django 3.1.5 on 2021-02-21 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210221_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='photo',
            new_name='photo',
        ),
    ]