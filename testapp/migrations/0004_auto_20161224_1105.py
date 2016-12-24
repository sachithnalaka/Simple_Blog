# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20161224_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Authors')),
            ],
        ),
        migrations.AddField(
            model_name='articals',
            name='comment_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testapp.Comments'),
            preserve_default=False,
        ),
    ]