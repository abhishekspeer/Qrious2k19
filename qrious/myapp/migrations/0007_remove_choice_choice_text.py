# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-23 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190123_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
    ]
