# Generated by Django 1.10 on 2016-08-27 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Derogation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('E', 'Eco'), ('H', 'Hors gel'), ('A', 'Arrêt')], default=None, max_length=1, verbose_name='mode de fonctionnement')),
                ('creation_dt', models.DateTimeField(auto_now_add=True, verbose_name='date/heure de création')),
                ('start_dt', models.DateTimeField(verbose_name="prise d'effet")),
                ('end_dt', models.DateTimeField(verbose_name="fin d'effet")),
            ],
            options={
                'ordering': ['creation_dt'],
            },
        ),
        migrations.CreateModel(
            name='PilotwireLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date/heure')),
                ('level', models.CharField(max_length=10, verbose_name='niveau')),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('E', 'Eco'), ('H', 'Hors gel'), ('A', 'Arrêt')], default=None, max_length=1, verbose_name='mode de fonctionnement')),
                ('mon', models.BooleanField(default=False, verbose_name='lundi')),
                ('tue', models.BooleanField(default=False, verbose_name='mardi')),
                ('wed', models.BooleanField(default=False, verbose_name='mercredi')),
                ('thu', models.BooleanField(default=False, verbose_name='jeudi')),
                ('fri', models.BooleanField(default=False, verbose_name='vendredi')),
                ('sat', models.BooleanField(default=False, verbose_name='samedi')),
                ('sun', models.BooleanField(default=False, verbose_name='dimanche')),
                ('start_time', models.TimeField(verbose_name='heure de début')),
                ('end_time', models.TimeField(verbose_name='heure de fin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('num', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], primary_key=True, serialize=False, verbose_name='numéro de zone')),
                ('desc', models.CharField(blank=True, max_length=50, verbose_name='description')),
            ],
            options={
                'ordering': ['num'],
            },
        ),
        migrations.AddField(
            model_name='slot',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heating.Zone'),
        ),
        migrations.AddField(
            model_name='derogation',
            name='zones',
            field=models.ManyToManyField(to='heating.Zone'),
        ),
    ]
