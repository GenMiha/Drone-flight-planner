# Generated by Django 4.1.3 on 2024-01-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droneSelling', '0009_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_goal', models.TextField(max_length=255, verbose_name='Request Goal')),
            ],
        ),
    ]
