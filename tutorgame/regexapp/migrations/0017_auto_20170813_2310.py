# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0016_auto_20170813_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_num',
            name='unique_id',
            field=models.CharField(default='Nv4m47PlwKOPuO7U4l20M03mf5qA9CXI', max_length=32, primary_key=True, serialize=False),
        ),
    ]
