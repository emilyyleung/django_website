# Generated by Django 3.0.3 on 2020-03-17 03:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20200317_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 17, 14, 22, 38, 788025), verbose_name='date published'),
        ),
    ]