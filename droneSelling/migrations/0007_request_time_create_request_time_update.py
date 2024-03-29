# Generated by Django 4.1.3 on 2022-12-18 22:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('droneSelling', '0006_contract_article_request_uav_uav_serial_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
