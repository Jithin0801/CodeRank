# Generated by Django 3.1.7 on 2021-03-31 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_module', '0022_auto_20210330_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practiceproblem',
            name='inputexplanation',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='practiceproblem',
            name='outputexplanation',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='practiceproblem',
            name='problemdescription',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='practiceproblem',
            name='problemexplanation',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='practiceproblem',
            name='problemstatement',
            field=models.TextField(max_length=1000),
        ),
    ]
