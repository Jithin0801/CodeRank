# Generated by Django 3.1.7 on 2021-03-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0003_blogmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
