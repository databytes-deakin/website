# Generated by Django 4.0.4 on 2022-05-15 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
