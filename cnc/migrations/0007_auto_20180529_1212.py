# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnc', '0006_auto_20180529_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=120)),
                ('data', models.CharField(max_length=80)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnc.Bot')),
            ],
        ),
        migrations.AddField(
            model_name='calllog',
            name='bot',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cnc.Bot', null=True),
            preserve_default=False,
        ),
    ]