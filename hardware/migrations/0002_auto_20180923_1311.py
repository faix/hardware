# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-09-23 20:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.RenameField( 'Lending', 'lending_by', 'borrowing_by'),
        migrations.RenameModel( 'Lending', 'Borrowing')
    ]
