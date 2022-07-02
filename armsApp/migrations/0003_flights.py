# Generated by Django 4.0.3 on 2022-04-27 05:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('armsApp', '0002_airport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250)),
                ('air_craft_code', models.CharField(max_length=250)),
                ('departure', models.DateTimeField()),
                ('estimated_arrival', models.DateTimeField()),
                ('slots', models.IntegerField()),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armsApp.airlines')),
                ('from_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From_Airport', to='armsApp.airport')),
                ('to_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To_Airport', to='armsApp.airport')),
            ],
            options={
                'verbose_name_plural': 'List of Airports',
            },
        ),
    ]