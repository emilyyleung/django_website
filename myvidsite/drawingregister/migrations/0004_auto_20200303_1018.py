# Generated by Django 3.0.3 on 2020-03-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawingregister', '0003_drawings_originator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawings',
            name='phase',
            field=models.CharField(choices=[('Design Development', 'Design Development')], default='Design Development', max_length=200),
        ),
    ]
