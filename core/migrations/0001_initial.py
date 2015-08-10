# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateTimeField(auto_now=True)),
                ('fecha_finalizacion', models.DateTimeField()),
                ('todo', models.TextField()),
                ('propietario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
