# Generated by Django 3.0.5 on 2020-06-12 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_auto_20200529_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]