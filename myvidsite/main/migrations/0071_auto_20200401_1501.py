# Generated by Django 3.0.3 on 2020-04-01 04:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0070_auto_20200401_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 15, 1, 35, 680640), verbose_name='date published'),
        ),
    ]