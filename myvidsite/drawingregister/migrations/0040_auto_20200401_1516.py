# Generated by Django 3.0.3 on 2020-04-01 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drawingregister', '0039_auto_20200401_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawings',
            name='project',
            field=models.ForeignKey(blank=True, default='000001.00 - test_project', null=True, on_delete=django.db.models.deletion.CASCADE, to='drawingregister.Projects'),
        ),
    ]
