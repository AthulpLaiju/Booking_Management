# Generated by Django 4.1.4 on 2023-02-16 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
        ),
        migrations.AddField(
            model_name='bookings',
            name='phno',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
        ),
    ]
