# Generated by Django 3.1.7 on 2021-03-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_module', '0010_practiceproblem_difficulty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practiceproblem',
            old_name='problemexplanation',
            new_name='problemedescription',
        ),
        migrations.AddField(
            model_name='practiceproblem',
            name='problemestatement',
            field=models.CharField(default=8, max_length=1000),
            preserve_default=False,
        ),
    ]