# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registration',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]