# Generated by Django 3.0.5 on 2020-04-26 03:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20200426_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='point_recieved',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)]),
        ),
    ]