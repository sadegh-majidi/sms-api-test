# Generated by Django 2.2.17 on 2021-02-04 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_receptor', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09011001010'. 11 digits allowed.", regex='^\\d{11}$')], verbose_name='receptor')),
                ('message', models.CharField(max_length=150, verbose_name='Message content')),
            ],
        ),
    ]
