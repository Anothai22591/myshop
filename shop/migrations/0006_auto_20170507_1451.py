# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170503_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_user',
            old_name='order_name',
            new_name='Order_user_text',
        ),
    ]
