# Generated by Django 3.1.7 on 2021-03-28 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compete_module', '0002_auto_20210328_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competemodel',
            old_name='competitionendingdate',
            new_name='competitionenddate',
        ),
        migrations.RenameField(
            model_name='competemodel',
            old_name='competitionstartingdate',
            new_name='competitionstartdate',
        ),
    ]
