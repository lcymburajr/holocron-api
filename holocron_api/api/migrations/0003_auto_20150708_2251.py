# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150702_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='placement_url',
            field=models.CharField(max_length=250),
        ),
    ]
