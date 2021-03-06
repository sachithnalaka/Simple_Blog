# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artical_title', models.CharField(max_length=50)),
                ('artical', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='articals',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Authors'),
        ),
    ]
