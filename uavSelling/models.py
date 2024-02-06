import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.CharField('article', max_length=10)
    contract_date = models.DateField('contract date')
    document = models.URLField('Document')


class DroneType(models.Model):
    model = models.CharField('model', max_length=12)
    description = models.TextField('description')
    rolled_up_state = models.CharField('rolled up state', max_length=30)
    deployed_state = models.CharField('deployed state', max_length=30)


class Drone(models.Model):
    name = models.CharField('drone', max_length=20)
    serial_number = models.CharField('serial number', default='0', max_length=15)
    description = models.TextField('description')
    manufacture_date = models.DateField('manufacture date')
    registration_date = models.DateField('registration date')
    status = models.TextField('status')
    drone_type_id = models.ForeignKey(DroneType, on_delete=models.CASCADE)


class TechCard(models.Model):
    description = models.CharField('description', max_length=20)
    dronetype_id = models.ForeignKey(DroneType, on_delete=models.CASCADE)


class TechOperation(models.Model):
    description = models.CharField('description', max_length=20)
    html_content = models.URLField('html-content')
    instruction_order = models.IntegerField('instruction order')
    techcard_id = models.ForeignKey(TechCard, on_delete=models.CASCADE)


class Request(models.Model):
    description = models.TextField('description', default=None)
    attachments = models.URLField('attachments', default='#')
    request_date = models.DateTimeField('request date', auto_now_add=True)
    response_date = models.DateTimeField('response date')
    repair_date = models.DateTimeField('repair date')
    status = models.TextField('status')
    summary = models.TextField('summary')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE)


class SimpleRequest(models.Model):
    request_goal = models.TextField(verbose_name='Request Goal', max_length=255)


class CompletedTechCard(models.Model):
    perform_date = models.DateTimeField('perform date')
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE)
    techcard_id = models.ForeignKey(TechCard, on_delete=models.CASCADE)


class CompletedTechOperation(models.Model):
    perform_date = models.DateTimeField('perform date')
    done_confirm_date = models.DateTimeField('done confirm date')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tech_oper_id = models.ForeignKey(TechOperation, on_delete=models.CASCADE)
    comp_techcard_id = models.ForeignKey(CompletedTechCard, on_delete=models.CASCADE)


class Service(models.Model):
    type = models.CharField('type', max_length=20)
    criteria = models.JSONField('criteria')
    drone_type_id = models.ForeignKey(DroneType, on_delete=models.CASCADE)
    techcard_id = models.ForeignKey(TechCard, on_delete=models.CASCADE)


class Flight(models.Model):
    start = models.DateTimeField('start')
    duration = models.FloatField('duration')
    status = models.CharField('status', max_length=10)
    reg_fly_info = models.BinaryField('reg fly info')
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE)





