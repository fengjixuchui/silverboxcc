# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnc', '0008_auto_20180529_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='botcommand',
            name='deployed',
            field=models.DateTimeField(null=True),
        ),
    ]