# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo_hecho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='hecho',
            field=models.BooleanField(default=False),
        ),
    ]
