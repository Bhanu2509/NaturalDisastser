# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etv', '0006_quaketsunami_volcanotsunami'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volcaniceruption',
            name='subtype',
            field=models.CharField(choices=[('m-Hawaiian', 'Magmatic Hawaiian'), ('m-Strombolian', 'Magmatic Strombolian'), ('m-Vulcanian', 'Magmatic Vulcanian'), ('m-Pelean', 'Magmatic Pelean'), ('p-Surtseyan', 'Phreatomagmatic Surtseyan'), ('p-Submarine', 'Phreatomagmatic Submarine'), ('p-Subglacial', 'Phreatomagmatic Subglacial')], max_length=256),
        ),
        migrations.AlterField(
            model_name='volcaniceruption',
            name='type',
            field=models.CharField(choices=[('magma', 'Magmatic eruption'), ('phreato', 'Phreatomagmatic eruption')], max_length=256),
        ),
    ]