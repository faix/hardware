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
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picked_up_time', models.DateTimeField(auto_now_add=True)),
                ('return_time', models.DateTimeField(blank=True, null=True)),
                ('borrowing_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hardware_admin_borrowing', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.Item')),
                ('return_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hardware_admin_return', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='lending',
            name='item',
        ),
        migrations.RemoveField(
            model_name='lending',
            name='lending_by',
        ),
        migrations.RemoveField(
            model_name='lending',
            name='return_by',
        ),
        migrations.RemoveField(
            model_name='lending',
            name='user',
        ),
        migrations.RemoveField(
            model_name='request',
            name='lending',
        ),
        migrations.DeleteModel(
            name='Lending',
        ),
        migrations.AddField(
            model_name='request',
            name='borrowing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hardware.Borrowing'),
        ),
    ]