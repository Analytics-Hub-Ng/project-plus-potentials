# Generated by Django 2.1.5 on 2019-02-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0021_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
