# Generated by Django 4.1.4 on 2022-12-22 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
        ),
    ]
