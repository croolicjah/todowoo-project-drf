# Generated by Django 3.1.5 on 2021-03-26 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20210221_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='photo',
        ),
    ]
