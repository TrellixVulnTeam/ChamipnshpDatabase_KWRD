# Generated by Django 3.2.3 on 2021-05-20 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210520_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('round_number', models.IntegerField()),
                ('file', models.FileField(unique=True, upload_to='')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.championship')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.session')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.track')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.year')),
            ],
            options={
                'unique_together': {('name', 'year', 'session', 'round_number', 'championship', 'track')},
                'index_together': {('name', 'year', 'session', 'round_number', 'championship', 'track')},
            },
        ),
    ]
