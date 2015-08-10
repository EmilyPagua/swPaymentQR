# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150804_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='fecha_finalizacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
