# Generated by Django 3.0.3 on 2020-03-27 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_auto_20200325_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 17, 15, 57, 459034), verbose_name='date published'),
        ),
    ]
