# Generated by Django 3.0.5 on 2020-04-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20200426_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
