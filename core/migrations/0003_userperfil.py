# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_remove_todo_otro'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPerfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField(null=True, blank=True)),
                ('is_company', models.BooleanField(default=False)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
