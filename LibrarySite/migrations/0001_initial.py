# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(default='Default title', max_length=50)),
                ('author', models.CharField(default='Default author', max_length=20)),
                ('genre', models.CharField(default='Default genre', max_length=20)),
                ('description', models.CharField(default='No description available', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('birthday', models.DateField(null=True)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=25)),
                ('studentNum', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
