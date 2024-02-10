# Generated by Django 4.1.3 on 2023-11-14 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('droneSelling', '0008_remove_request_time_create_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='DateTime Notice')),
                ('notice', models.TextField(max_length=250, verbose_name='Notice')),
                ('uav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='droneSelling.uav')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]