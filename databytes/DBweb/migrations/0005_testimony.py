# Generated by Django 4.0.4 on 2022-05-25 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0004_rename_jobdesc_job_jobdescription_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('TestimonyID', models.AutoField(primary_key=True, serialize=False)),
                ('TestimonyName', models.CharField(max_length=64)),
                ('TestimonyTitle', models.CharField(max_length=64)),
                ('TestimonyQuote', models.TextField(max_length=512)),
            ],
        ),
    ]
