# Generated by Django 3.0.6 on 2021-03-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20210304_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datetime',
            field=models.DateField(blank=True),
        ),
    ]
