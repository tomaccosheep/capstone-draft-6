# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0036_auto_20170814_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_num',
            name='full_string',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='game_num',
            name='repeat_me',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='game_num',
            name='select_me',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='game_num',
            name='unique_id',
            field=models.CharField(default='w1sqwkfo4M65QkfU8VvFMApvTyJNq4Uo', max_length=32, primary_key=True, serialize=False),
        ),
    ]
