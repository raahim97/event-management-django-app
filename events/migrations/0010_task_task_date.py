# Generated by Django 3.0.5 on 2020-04-26 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20200426_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
