# Generated by Django 2.2.7 on 2019-12-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
