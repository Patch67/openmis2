# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='biography',
            field=models.TextField(default='My Blog'),
            preserve_default=False,
        ),
    ]