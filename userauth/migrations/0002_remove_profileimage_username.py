# Generated by Django 4.1.1 on 2022-09-27 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimage',
            name='username',
        ),
    ]
