# Generated by Django 3.1.7 on 2021-04-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler_module', '0007_auto_20210406_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='competeproblemresult',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='practiceproblemresult',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]