# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_books_in_print'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='in_print',
        ),
        migrations.RemoveField(
            model_name='books',
            name='publish_date',
        ),
    ]
