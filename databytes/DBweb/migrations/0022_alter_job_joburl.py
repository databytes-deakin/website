# Generated by Django 4.1 on 2022-09-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0021_alter_job_joburl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='JobURL',
            field=models.CharField(default='<django.db.models.fields.CharField>', max_length=64),
        ),
    ]
