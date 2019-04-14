# Generated by Django 2.1.5 on 2019-02-23 05:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0018_auto_20190223_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_article',
            field=tinymce.models.HTMLField(default='', verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
