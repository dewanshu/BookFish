# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-10 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswap', '0003_mister'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='final',
            field=models.CharField(default='hello', max_length=30),
            preserve_default=False,
        ),
    ]
