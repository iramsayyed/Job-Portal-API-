# Generated by Django 4.1.1 on 2022-09-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_rename_skill_userskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]