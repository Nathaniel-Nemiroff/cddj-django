# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='likenum',
            field=models.IntegerField(default=0),
        ),
    ]
