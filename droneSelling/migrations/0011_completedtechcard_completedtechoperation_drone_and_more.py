# Generated by Django 4.1.3 on 2024-02-05 14:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('droneSelling', '0010_simplerequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTechCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perform_date', models.DateTimeField(verbose_name='perform date')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedTechOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perform_date', models.DateTimeField(verbose_name='perform date')),
                ('done_confirm_date', models.DateTimeField(verbose_name='done confirm date')),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='drone')),
                ('serial_number', models.CharField(default='0', max_length=15, verbose_name='serial number')),
                ('description', models.TextField(verbose_name='description')),
                ('manufacture_date', models.DateField(verbose_name='manufacture date')),
                ('registration_date', models.DateField(verbose_name='registration date')),
                ('status', models.TextField(verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='DroneType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=12, verbose_name='model')),
                ('description', models.TextField(verbose_name='description')),
                ('rolled_up_state', models.CharField(max_length=30, verbose_name='rolled up state')),
                ('deployed_state', models.CharField(max_length=30, verbose_name='deployed state')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='start')),
                ('duration', models.FloatField(verbose_name='duration')),
                ('status', models.CharField(max_length=10, verbose_name='status')),
                ('reg_fly_info', models.BinaryField(verbose_name='reg fly info')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='type')),
                ('criteria', models.JSONField(verbose_name='criteria')),
            ],
        ),
        migrations.CreateModel(
            name='TechCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction_order', models.IntegerField(verbose_name='instruction order')),
            ],
        ),
        migrations.CreateModel(
            name='TechOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='electroniccard',
            name='uav',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='uav',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.RemoveField(
            model_name='partreplace',
            name='parts',
        ),
        migrations.RemoveField(
            model_name='partreplace',
            name='request',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='charger',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='engine',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='nozzles',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='propeller',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='pump',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='remote_control',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='tank',
        ),
        migrations.RemoveField(
            model_name='parts',
            name='uav',
        ),
        migrations.RemoveField(
            model_name='repairing',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='repairing',
            name='parts',
        ),
        migrations.RemoveField(
            model_name='repairing',
            name='request',
        ),
        migrations.RemoveField(
            model_name='techservice',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='techservice',
            name='request',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_goal',
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_type',
        ),
        migrations.RemoveField(
            model_name='request',
            name='uav',
        ),
        migrations.AddField(
            model_name='request',
            name='attachments',
            field=models.URLField(default='#', verbose_name='attachments'),
        ),
        migrations.AddField(
            model_name='request',
            name='description',
            field=models.TextField(default=None, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='request',
            name='repair_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='repair date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 17, 37, 18, 243023), verbose_name='request date'),
        ),
        migrations.AddField(
            model_name='request',
            name='response_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='response date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='summary',
            field=models.TextField(default='summary', verbose_name='summary'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='article',
            field=models.CharField(max_length=10, verbose_name='article'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(verbose_name='contract date'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.TextField(verbose_name='status'),
        ),
        migrations.DeleteModel(
            name='Battery',
        ),
        migrations.DeleteModel(
            name='Charger',
        ),
        migrations.DeleteModel(
            name='ElectronicCard',
        ),
        migrations.DeleteModel(
            name='Engine',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Nozzles',
        ),
        migrations.DeleteModel(
            name='PartReplace',
        ),
        migrations.DeleteModel(
            name='Parts',
        ),
        migrations.DeleteModel(
            name='Propeller',
        ),
        migrations.DeleteModel(
            name='Pump',
        ),
        migrations.DeleteModel(
            name='RemoteControl',
        ),
        migrations.DeleteModel(
            name='Repairing',
        ),
        migrations.DeleteModel(
            name='Tank',
        ),
        migrations.DeleteModel(
            name='TechService',
        ),
        migrations.DeleteModel(
            name='UAV',
        ),
        migrations.AddField(
            model_name='techcard',
            name='tech_op_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.techoperation'),
        ),
        migrations.AddField(
            model_name='service',
            name='tech_card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.techcard'),
        ),
        migrations.AddField(
            model_name='dronetype',
            name='tech_card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.techcard'),
        ),
        migrations.AddField(
            model_name='completedtechoperation',
            name='tech_oper_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.techoperation'),
        ),
        migrations.AddField(
            model_name='completedtechoperation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='completedtechcard',
            name='comp_tech_oper_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.completedtechoperation'),
        ),
        migrations.AddField(
            model_name='completedtechcard',
            name='drone_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.drone'),
        ),
        migrations.AddField(
            model_name='completedtechcard',
            name='tech_card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.techcard'),
        ),
        migrations.AddField(
            model_name='request',
            name='drone_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='droneSelling.drone'),
            preserve_default=False,
        ),
    ]
