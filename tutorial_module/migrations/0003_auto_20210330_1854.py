# Generated by Django 3.1.7 on 2021-03-30 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_module', '0022_auto_20210330_1422'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorial_module', '0002_auto_20210330_1714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TutorialCompletedStatus',
            new_name='MaintopicCompletedStatus',
        ),
        migrations.RemoveField(
            model_name='maintopiccompletedstatus',
            name='tutorialsubtopic',
        ),
        migrations.AddField(
            model_name='maintopiccompletedstatus',
            name='maintopic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='practice_module.practicemaintopic'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TutorialSubtopicCompletedStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iscompleted', models.BooleanField(default=0)),
                ('tutorialsubtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial_module.tutorialsubtopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubtopicCompletedStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iscompleted', models.BooleanField(default=0)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice_module.practicesubtopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
