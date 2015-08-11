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
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_card', models.IntegerField()),
                ('name_card', models.TextField()),
                ('expiration_year', models.DateField()),
                ('available', models.IntegerField()),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateTimeField(auto_now=True)),
                ('fecha_finalizacion', models.DateTimeField(null=True, blank=True)),
                ('todo', models.TextField()),
                ('otro', models.TextField(default=b'defa')),
                ('hecho', models.BooleanField(default=False)),
                ('propietario', models.ForeignKey(related_name='propietario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_transaction', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('card', models.ForeignKey(related_name='card', to='core.Card')),
                ('collect', models.ForeignKey(related_name='collect', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='type_card',
            field=models.ForeignKey(related_name='type_card', to='core.TypeCard'),
        ),
    ]
