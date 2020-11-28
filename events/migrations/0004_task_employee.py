# Generated by Django 3.0.5 on 2020-04-25 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20200426_0137'),
        ('events', '0003_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='employees.Employee'),
            preserve_default=False,
        ),
    ]