# Generated by Django 4.0.4 on 2022-08-17 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0004_alter_myuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
    ]
