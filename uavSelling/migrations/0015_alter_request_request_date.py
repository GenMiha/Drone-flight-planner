# Generated by Django 4.1.3 on 2024-02-06 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uavSelling', '0014_techoperation_html_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 20, 4, 20, 304503), verbose_name='request date'),
        ),
    ]