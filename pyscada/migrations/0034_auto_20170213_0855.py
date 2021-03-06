# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0033_auto_20161107_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[(b'generic', b'no Protocol'), (b'systemstat', b'Local System Monitoring'), (b'modbus', b'Modbus Device'), (b'smbus', b'SMBus/I2C Device'), (b'phant', b'Phant Device'), (b'visa', b'VISA Device'), (b'onewire', b'1-Wire Device')], default=b'generic', max_length=400),
        ),
    ]
