# Generated by Django 4.0.6 on 2022-08-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0010_project_projectenddate_project_projectstartdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ProjectIsActive',
            field=models.BooleanField(default=True),
        ),
    ]
