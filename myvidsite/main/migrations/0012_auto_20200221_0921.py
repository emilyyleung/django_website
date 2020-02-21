# Generated by Django 3.0.3 on 2020-02-20 22:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200221_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 21, 9, 21, 35, 411416), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.TutorialCategory', verbose_name='Category'),
        ),
    ]
