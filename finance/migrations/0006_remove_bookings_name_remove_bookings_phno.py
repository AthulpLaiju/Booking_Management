# Generated by Django 4.1.4 on 2023-02-16 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_bookings_name_bookings_phno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='phno',
        ),
    ]
