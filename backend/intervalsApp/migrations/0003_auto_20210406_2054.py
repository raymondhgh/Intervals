# Generated by Django 3.1.6 on 2021-04-07 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intervalsApp', '0002_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='profile',
        ),
    ]
