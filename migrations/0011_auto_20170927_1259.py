# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-27 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20170927_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes',
            name='sity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Sity'),
        ),
    ]
