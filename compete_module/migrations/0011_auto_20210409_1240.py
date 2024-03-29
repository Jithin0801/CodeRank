# Generated by Django 3.1.7 on 2021-04-09 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compete_module', '0010_auto_20210409_0228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='inputexplanation',
            new_name='input_explanation',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='outputexplanation',
            new_name='output_explanation',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemconstraints',
            new_name='problem_constraints',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemdescription',
            new_name='problem_description',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemexplanation',
            new_name='problem_explanation',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemstatement',
            new_name='problem_statement',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemtestcaseoneinput',
            new_name='problem_testcase_one_input',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemtestcaseoneoutput',
            new_name='problem_testcase_one_output',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemtestcasethreeinput',
            new_name='problem_testcase_three_input',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemtestcasethreeoutput',
            new_name='problem_testcase_three_output',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemtestcasetwoinput',
            new_name='problem_testcase_two_input',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemtestcasetwooutput',
            new_name='problem_testcase_two_output',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='problemtitle',
            new_name='problem_title',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='sampleinput',
            new_name='sample_input',
        ),
        migrations.RenameField(
            model_name='competitionownproblem',
            old_name='sampleoutput',
            new_name='sample_output',
        ),
    ]
