# Generated by Django 3.1.7 on 2021-03-25 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice_module', '0017_auto_20210325_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practiceproblem',
            old_name='problemedescription',
            new_name='problemdescription',
        ),
        migrations.RenameField(
            model_name='practiceproblem',
            old_name='problemestatement',
            new_name='problemstatement',
        ),
    ]