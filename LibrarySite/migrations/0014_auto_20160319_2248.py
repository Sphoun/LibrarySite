# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibrarySite', '0013_auto_20160319_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='studentNum',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='LibrarySite/media', default='LibrarySite/media/book.jpg'),
        ),
    ]
