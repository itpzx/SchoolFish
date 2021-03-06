# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-14 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('comid', models.IntegerField(primary_key=True, serialize=False)),
                ('comname', models.CharField(max_length=50)),
                ('comdescribe', models.CharField(max_length=300)),
                ('complace', models.CharField(max_length=50)),
                ('userid', models.IntegerField()),
                ('userqq', models.CharField(max_length=20)),
                ('usertel', models.CharField(max_length=20)),
                ('dtime', models.DateField(auto_now_add=True)),
                ('commoney', models.FloatField()),
                ('comtype', models.CharField(max_length=50)),
            ],
            managers=[
                ('coms', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('conid', models.IntegerField(primary_key=True, serialize=False)),
                ('conpwd', models.CharField(max_length=30)),
                ('conname', models.CharField(max_length=20)),
                ('command', models.CharField(max_length=20, null=True)),
            ],
            managers=[
                ('cons', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('userpwd', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
            ],
            managers=[
                ('users', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Usercom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('comid', models.IntegerField()),
            ],
            managers=[
                ('usercoms', django.db.models.manager.Manager()),
            ],
        ),
    ]
