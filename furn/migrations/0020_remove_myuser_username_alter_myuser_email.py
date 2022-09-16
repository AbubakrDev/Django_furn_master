# Generated by Django 4.1 on 2022-08-31 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0019_myuser_username_alter_myuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
