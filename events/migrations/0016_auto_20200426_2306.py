# Generated by Django 3.0.5 on 2020-04-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20200426_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
