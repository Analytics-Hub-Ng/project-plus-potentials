# Generated by Django 2.1.5 on 2019-02-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0006_project_project_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='service_image1',
            field=models.ImageField(default='serviceimages/None/no-img.jpg', upload_to='serviceimages/'),
        ),
    ]
