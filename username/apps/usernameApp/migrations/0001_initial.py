# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=26)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
