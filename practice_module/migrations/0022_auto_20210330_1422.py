# Generated by Django 3.1.7 on 2021-03-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice_module', '0021_auto_20210326_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practiceproblem',
            old_name='topic',
            new_name='subtopic',
        ),
    ]
