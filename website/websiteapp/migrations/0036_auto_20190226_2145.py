# Generated by Django 2.1.5 on 2019-02-26 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0035_auto_20190226_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ProjectDetailContent',
        ),
        migrations.DeleteModel(
            name='ProjectDetailContent',
        ),
    ]
