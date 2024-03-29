# Generated by Django 4.1.4 on 2023-02-24 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_remove_bookings_name_remove_bookings_phno'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
        ),
        migrations.AddField(
            model_name='bookings',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
        ),
        migrations.AddField(
            model_name='bookings',
            name='phon',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
        ),
    ]
