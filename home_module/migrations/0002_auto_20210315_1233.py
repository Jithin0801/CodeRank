# Generated by Django 3.1.7 on 2021-03-15 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DSChallenge',
            new_name='AlgorithmTopic',
        ),
        migrations.RenameModel(
            old_name='AlgorithmChallenge',
            new_name='DSTopic',
        ),
        migrations.RenameField(
            model_name='algorithmtopic',
            old_name='dscontent',
            new_name='algocontent',
        ),
        migrations.RenameField(
            model_name='algorithmtopic',
            old_name='dstitle',
            new_name='algotitle',
        ),
        migrations.RenameField(
            model_name='dstopic',
            old_name='algocontent',
            new_name='dscontent',
        ),
        migrations.RenameField(
            model_name='dstopic',
            old_name='algotitle',
            new_name='dstitle',
        ),
    ]