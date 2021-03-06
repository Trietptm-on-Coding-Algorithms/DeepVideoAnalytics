# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdnapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='aws_bucket',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='dataset',
            name='aws_key',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='dataset',
            name='aws_region',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='dataset',
            name='aws_requester_pays',
            field=models.BooleanField(default=False),
        ),
    ]
