# Generated by Django 4.1.3 on 2024-02-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droneSelling', '0023_alter_request_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.TextField(choices=[('ACTIVE', 'Active'), ('DECLINED', 'Declined'), ('COMPLETED', 'Completed')], default='ACTIVE', verbose_name='status'),
        ),
    ]
