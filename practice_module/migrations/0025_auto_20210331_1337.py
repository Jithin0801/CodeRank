# Generated by Django 3.1.7 on 2021-03-31 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice_module', '0024_auto_20210331_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practiceproblem',
            name='userestcaseoneoutput',
        ),
        migrations.RemoveField(
            model_name='practiceproblem',
            name='userestcasethreeoutput',
        ),
        migrations.RemoveField(
            model_name='practiceproblem',
            name='userestcasetwooutput',
        ),
    ]
