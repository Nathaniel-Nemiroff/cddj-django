# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20170620_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='in_print',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]