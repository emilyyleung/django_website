# Generated by Django 3.0.3 on 2020-02-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawingregister', '0002_auto_20200228_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawings',
            name='originator',
            field=models.CharField(default='Cox Architects', max_length=200),
        ),
    ]
