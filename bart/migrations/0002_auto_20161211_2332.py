# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='command',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
