# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='visible_after',
            field=models.TimeField(),
        ),
    ]
