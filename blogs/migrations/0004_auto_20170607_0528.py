# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20170606_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markpost',
            name='status',
            field=models.BooleanField(choices=[(False, 'Не прочитано'), (True, 'Прочитано')], default=False, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='subscribeblog',
            name='status',
            field=models.BooleanField(choices=[(False, 'Не подписан'), (True, 'Подписан')], default=False, verbose_name='Статус подписки'),
        ),
    ]
