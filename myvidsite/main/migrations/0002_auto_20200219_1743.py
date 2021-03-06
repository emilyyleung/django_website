# Generated by Django 3.0.3 on 2020-02-19 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 17, 43, 44, 135471), verbose_name='date published'),
        ),
    ]
