# Generated by Django 3.1.7 on 2021-03-28 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compete_module', '0003_auto_20210328_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competemodel',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
