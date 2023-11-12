# Generated by Django 4.2.7 on 2023-11-12 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_trip_seats_alter_trip_driver_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='car',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='trip.car'),
            preserve_default=False,
        ),
    ]
