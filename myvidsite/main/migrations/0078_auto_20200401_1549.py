# Generated by Django 3.0.3 on 2020-04-01 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0077_auto_20200401_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 15, 49, 40, 719423), verbose_name='date published'),
        ),
    ]
