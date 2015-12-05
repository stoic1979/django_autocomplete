# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Please input full name, that way system will recognize recurring customer', max_length=12, null=True, verbose_name=b'customer name', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('address_street', models.CharField(max_length=100, verbose_name=b'Street')),
                ('address_house', models.CharField(max_length=10, verbose_name=b'House')),
                ('address_flat', models.CharField(max_length=20, null=True, verbose_name=b'Flat', blank=True)),
                ('address_postal_code', models.CharField(max_length=20, null=True, verbose_name=b'Postal code', blank=True)),
                ('address_comment', models.CharField(default=b'', max_length=12, null=True, verbose_name=b'Comments', blank=True)),
                ('phone', models.CharField(max_length=12, verbose_name=b'phone')),
            ],
        ),
    ]
