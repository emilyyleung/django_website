# Generated by Django 3.0.3 on 2020-03-31 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawingregister', '0028_auto_20200331_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawings',
            name='dn_discipline',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='dn_level',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='dn_originator',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='dn_project',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='dn_series',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='dn_type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='dn_volume_system',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='dn_zone_sequence',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='model_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]