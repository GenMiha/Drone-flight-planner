from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models


class User(AbstractUser):
    name = models.CharField(verbose_name='Name', max_length=20, blank=True, null=True)
    surname = models.CharField(verbose_name='Surname', max_length=35, blank=True, null=True)
    user_email = models.CharField(verbose_name='EMAIL', max_length=100, blank=True, null=True)


class Charger(models.Model):
    name = models.CharField(verbose_name='Charger')
    input_voltage = models.CharField(verbose_name='Input Voltage', max_length=20)
    output_voltage = models.CharField(verbose_name='Output Voltage', max_length=20)
    power_output = models.IntegerField(verbose_name='Power', validators=[MinValueValidator(0)])
    weight = models.IntegerField(verbose_name='Weight', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.CharField(verbose_name='Status')


class RemoteControl(models.Model):
    name = models.CharField(verbose_name='Remote control')
    description = models.CharField(verbose_name='Description', max_length=255)
    price = models.IntegerField(verbose_name='Price')
    status = models.CharField(verbose_name='Status')


class Battery(models.Model):
    name = models.CharField(verbose_name='Battery')
    min_capacity = models.IntegerField(verbose_name='Minimal capacity', validators=[MinValueValidator(0)])
    configuration = models.CharField(verbose_name='Configuration', max_length=15)
    weight = models.FloatField(verbose_name='Weight', validators=[MinValueValidator(0)])
    length = models.FloatField(verbose_name='Length', validators=[MinValueValidator(0)])
    width = models.FloatField(verbose_name='Width', validators=[MinValueValidator(0)])
    height = models.FloatField(verbose_name='Height', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.CharField(verbose_name='Status')


class Propeller(models.Model):
    name = models.CharField(verbose_name='Propeller')
    diameter_step = models.CharField(verbose_name='Diameter*Step')
    price = models.IntegerField(verbose_name='Price')
    status = models.CharField(verbose_name='Status')


class Tank(models.Model):
    name = models.CharField(verbose_name='Tank')
    capacity = models.IntegerField(verbose_name='Capacity', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.CharField(verbose_name='Status')


class Nozzles(models.Model):
    name = models.CharField(verbose_name='Nozzles')
    description = models.CharField(verbose_name='Description', max_length=255)
    price = models.IntegerField(verbose_name='Price')
    status = models.CharField(verbose_name='Status')


class Engine(models.Model):
    name = models.CharField(verbose_name='Remote control')
    max_pull = models.FloatField(verbose_name='Max Pull per Axis', validators=[MinValueValidator(0)])
    recomended_weight = models.FloatField(verbose_name='Recomended weight per Axis', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.CharField(verbose_name='Status')


class UAV(models.Model):
    model = models.CharField(verbose_name='Model')


class Request(models.Model):
    request_goal = models.CharField(verbose_name='Request Goal', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Status', max_length=15)



