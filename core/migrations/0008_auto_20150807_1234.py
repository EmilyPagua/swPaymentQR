# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_todo_fecha_finalizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='fecha_finalizacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='propietario',
            field=models.ForeignKey(related_name='propietario', to=settings.AUTH_USER_MODEL),
        ),
    ]
