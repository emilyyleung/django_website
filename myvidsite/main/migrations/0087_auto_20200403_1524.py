# Generated by Django 3.0.3 on 2020-04-03 04:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0086_auto_20200403_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 15, 24, 28, 61551), verbose_name='date published'),
        ),
    ]
