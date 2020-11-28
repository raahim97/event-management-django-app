# Generated by Django 3.0.5 on 2020-04-26 03:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_task_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='percentage',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='point_recieved',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)]),
        ),
    ]