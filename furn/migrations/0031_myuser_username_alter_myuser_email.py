# Generated by Django 4.1 on 2022-09-14 11:42

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0030_ratestar'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=1, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]