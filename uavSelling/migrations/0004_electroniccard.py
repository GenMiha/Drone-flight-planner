# Generated by Django 4.1.3 on 2022-12-06 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uavSelling', '0003_request_techservice_repairing_partreplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.URLField(verbose_name='Document')),
                ('uav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uavSelling.uav')),
            ],
        ),
    ]
