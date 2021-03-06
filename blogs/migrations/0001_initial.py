# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Наименование блога')),
                ('description', models.TextField(verbose_name='Описание блога')),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Наименование поста')),
                ('description', models.TextField(verbose_name='Содержание поста')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog', verbose_name='Блог')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=40, unique=True, verbose_name='Уникальное имя пользователя')),
                ('first_name', models.CharField(max_length=40, verbose_name='Фамилия пользователя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Адрес электронной почты')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.User'),
        ),
    ]
