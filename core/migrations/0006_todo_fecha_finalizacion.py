# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_todo_fecha_finalizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='fecha_finalizacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
