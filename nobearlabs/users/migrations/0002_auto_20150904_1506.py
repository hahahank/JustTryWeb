# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bank_id_first',
            field=models.CharField(blank=True, help_text='Required. digits only.', max_length=3, verbose_name='bank number', validators=[django.core.validators.RegexValidator(b'^[0-9]+$', 'Enter a valid bank id number.', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bank_id_last',
            field=models.CharField(blank=True, help_text='Required. digits only.', max_length=3, verbose_name='bank account', validators=[django.core.validators.RegexValidator(b'^[0-9]+$', 'Enter a valid bank account id number.', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='home_address',
            field=models.CharField(max_length=60, verbose_name='home address', blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(blank=True, help_text='Required. digits and +-() only.', max_length=30, verbose_name='mobile number', validators=[django.core.validators.RegexValidator(b'^[0-9+()-]+$', 'Enter a valid mobile number.', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Required. digits and +-() only.', max_length=30, verbose_name='home phone number', validators=[django.core.validators.RegexValidator(b'^[0-9+()-]+$', 'Enter a valid phone number.', b'invalid')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(unique=True, max_length=30, verbose_name='user name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='zip_code',
            field=models.CharField(blank=True, help_text='Required. digits only.', max_length=5, verbose_name='zip code', validators=[django.core.validators.RegexValidator(b'^[0-9]+$', 'Enter a valid bank number.', b'invalid')]),
        ),
    ]
