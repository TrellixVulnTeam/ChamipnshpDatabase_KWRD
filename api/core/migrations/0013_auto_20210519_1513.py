# Generated by Django 3.2.3 on 2021-05-19 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_year_year_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date_of_event',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='time_of_event',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
