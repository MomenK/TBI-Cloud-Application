# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ECoG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(verbose_name='date published')),
                ('Value1', models.IntegerField(default=0)),
                ('Value2', models.IntegerField(default=0)),
            ],
        ),
    ]
