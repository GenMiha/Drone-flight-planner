# Generated by Django 4.1.3 on 2024-02-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droneSelling', '0025_alter_drone_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='registration_date',
            field=models.DateField(auto_now_add=True, verbose_name='registration date'),
        ),
    ]
