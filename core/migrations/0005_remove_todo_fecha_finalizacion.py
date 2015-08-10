# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150807_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='fecha_finalizacion',
        ),
    ]
