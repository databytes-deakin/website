# Generated by Django 4.0.4 on 2022-05-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0002_rename_jobs_job_rename_projects_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='JobDesc',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectDesc',
            field=models.TextField(max_length=512),
        ),
    ]
