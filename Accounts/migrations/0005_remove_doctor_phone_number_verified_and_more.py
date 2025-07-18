# Generated by Django 4.2.6 on 2025-06-12 15:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_doctor_phone_number_verified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='phone_number_verified',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_number_verified',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
