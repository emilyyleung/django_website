# Generated by Django 3.0.3 on 2020-03-24 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20200324_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 14, 21, 9, 671727), verbose_name='date published'),
        ),
    ]
