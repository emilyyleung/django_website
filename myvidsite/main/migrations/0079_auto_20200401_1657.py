# Generated by Django 3.0.3 on 2020-04-01 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0078_auto_20200401_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 16, 57, 14, 708193), verbose_name='date published'),
        ),
    ]
