# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-09 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_auto_20190705_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='pass_word',
            new_name='password',
        ),
    ]