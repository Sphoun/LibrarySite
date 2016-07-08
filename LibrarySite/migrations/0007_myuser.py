# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LibrarySite', '0006_auto_20160316_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('birthday', models.DateField(null=True)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=25)),
                ('studentNum', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
