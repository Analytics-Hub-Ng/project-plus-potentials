# Generated by Django 2.1.5 on 2019-02-26 19:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0030_auto_20190226_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdetailcontent',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='ProjectDetailContent',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='websiteapp.ProjectDetailContent'),
            preserve_default=False,
        ),
    ]
