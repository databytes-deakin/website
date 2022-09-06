# Generated by Django 4.0.4 on 2022-08-23 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0014_alter_project_leaderemail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ProjectIsFeatured',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='ProjectShortDescription',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='LeaderEmail',
            field=models.EmailField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectDescription',
            field=models.TextField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectLeader',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectStartDate',
            field=models.DateTimeField(null=True),
        ),
    ]