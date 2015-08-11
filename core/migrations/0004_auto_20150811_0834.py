# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userperfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperfil',
            name='code',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
