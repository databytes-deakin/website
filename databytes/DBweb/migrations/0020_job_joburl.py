# Generated by Django 4.1 on 2022-09-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0019_project_projecturl'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='JobURL',
            field=models.CharField(default='<django.db.models.fields.CharField>', max_length=64),
        ),
    ]
