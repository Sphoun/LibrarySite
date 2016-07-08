# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibrarySite', '0015_auto_20160320_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='birthday',
        ),
    ]
