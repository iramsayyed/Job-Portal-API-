# Generated by Django 4.1.1 on 2022-09-27 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('userauth', '0003_skill'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skill',
            new_name='UserSkill',
        ),
    ]