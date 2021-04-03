# Generated by Django 3.1.7 on 2021-03-30 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('practice_module', '0022_auto_20210330_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialSubtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice_module.practicesubtopic')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000)),
                ('exampleone', models.CharField(max_length=2000)),
                ('exampletwo', models.CharField(max_length=2000)),
                ('tutorialsubtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial_module.tutorialsubtopic')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialCompletedStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iscompleted', models.BooleanField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
