# Generated by Django 4.1.4 on 2023-02-16 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remainder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Remainder',
        ),
    ]
