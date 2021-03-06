# Generated by Django 3.0.3 on 2020-02-19 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200220_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='slug',
            new_name='tutorial_slug',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 10, 11, 15, 150886), verbose_name='date published'),
        ),
    ]
