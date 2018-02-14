# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=350)),
                ('last_name', models.CharField(max_length=330)),
                ('movie_title', models.CharField(max_length=5000)),
                ('character', models.CharField(max_length=5000)),
                ('empty', models.CharField(max_length=5000)),
                ('role', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Actress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=350)),
                ('last_name', models.CharField(max_length=330)),
                ('movie_title', models.CharField(max_length=5000)),
                ('character', models.CharField(max_length=5000)),
                ('empty', models.CharField(max_length=5000)),
                ('role', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=350)),
                ('last_name', models.CharField(max_length=330)),
                ('movie_title', models.CharField(max_length=2250)),
                ('segment', models.CharField(max_length=1250)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_title', models.CharField(max_length=2250)),
                ('category', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Movieslist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_with_episode', models.CharField(max_length=5000)),
                ('movie_title', models.CharField(max_length=2000)),
                ('noo', models.CharField(max_length=500)),
                ('episode', models.CharField(max_length=2250)),
                ('season_id', models.CharField(max_length=225)),
                ('nooo', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_title', models.CharField(max_length=2250)),
                ('description', models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distribution', models.CharField(max_length=500)),
                ('votes', models.CharField(max_length=300)),
                ('rating', models.CharField(max_length=250)),
                ('movie_title', models.CharField(max_length=1250)),
            ],
        ),
    ]
