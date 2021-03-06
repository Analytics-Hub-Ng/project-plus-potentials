# Generated by Django 2.1.5 on 2019-02-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0010_auto_20190210_0453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['project_date']},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['service_title']},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['order_of_appearance_on_website']},
        ),
        migrations.AddField(
            model_name='staff',
            name='order_of_appearance_on_website',
            field=models.IntegerField(default=99, max_length=2),
            preserve_default=False,
        ),
    ]
