# Generated by Django 3.0.3 on 2020-03-31 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_auto_20200331_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 16, 21, 29, 35808), verbose_name='date published'),
        ),
    ]