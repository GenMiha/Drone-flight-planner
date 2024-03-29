# Generated by Django 4.1.3 on 2024-02-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droneSelling', '0024_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='status',
            field=models.TextField(choices=[('NEW', 'New'), ('IN USE', 'In Use'), ('ON SERVICE', 'On Service'), ('DECOMMISSIONED', 'Decommissioned')], default='NEW', verbose_name='status'),
        ),
    ]
