# Generated by Django 4.1.3 on 2024-02-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uavSelling', '0017_alter_request_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='request date'),
        ),
    ]
