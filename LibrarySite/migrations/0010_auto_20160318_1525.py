# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibrarySite', '0009_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.CharField(max_length=20, default='Not available'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=20, default='Not available'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=150, default='Not available'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=20, default='Not available'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, default='Not available'),
        ),
    ]
