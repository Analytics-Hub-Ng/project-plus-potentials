# Generated by Django 2.1.5 on 2019-02-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0025_auto_20190224_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='industry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Industrieses', to='websiteapp.Industry'),
        ),
    ]
