# Generated by Django 2.1.5 on 2019-02-25 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0027_auto_20190224_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='industry',
            options={'ordering': ['industry']},
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteapp.Project'),
        ),
    ]
