# Generated by Django 4.1.1 on 2022-09-27 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_rename_user_id_userskill_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userskill',
            name='skill',
        ),
    ]