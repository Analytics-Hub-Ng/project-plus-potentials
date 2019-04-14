# Generated by Django 2.1.5 on 2019-02-26 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0028_auto_20190225_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetailContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(default='Project', max_length=100)),
                ('sub_title', models.CharField(default='Project', max_length=100)),
                ('short_intro', models.CharField(default='We see your project from start to finish.', max_length=540)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteapp.Project')),
            ],
        ),
    ]