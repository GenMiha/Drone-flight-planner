from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Charger(models.Model):
    name = models.TextField(verbose_name='Charger')
    input_voltage = models.TextField(verbose_name='Input Voltage', max_length=20)
    output_voltage = models.TextField(verbose_name='Output Voltage', max_length=20)
    power_output = models.IntegerField(verbose_name='Power', validators=[MinValueValidator(0)])
    weight = models.IntegerField(verbose_name='Weight', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class RemoteControl(models.Model):
    name = models.TextField(verbose_name='Remote control')
    description = models.TextField(verbose_name='Description', max_length=255)
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class Battery(models.Model):
    name = models.TextField(verbose_name='Battery')
    min_capacity = models.IntegerField(verbose_name='Minimal capacity', validators=[MinValueValidator(0)])
    configuration = models.TextField(verbose_name='Configuration', max_length=15)
    weight = models.FloatField(verbose_name='Weight', validators=[MinValueValidator(0)])
    length = models.FloatField(verbose_name='Length', validators=[MinValueValidator(0)])
    width = models.FloatField(verbose_name='Width', validators=[MinValueValidator(0)])
    height = models.FloatField(verbose_name='Height', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class Propeller(models.Model):
    name = models.TextField(verbose_name='Propeller')
    diameter_step = models.TextField(verbose_name='Diameter*Step')
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class Tank(models.Model):
    name = models.TextField(verbose_name='Tank')
    capacity = models.IntegerField(verbose_name='Capacity', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class Nozzles(models.Model):
    name = models.TextField(verbose_name='Nozzles')
    description = models.TextField(verbose_name='Description', max_length=255)
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class Engine(models.Model):
    name = models.TextField(verbose_name='Remote control')
    max_pull = models.FloatField(verbose_name='Max Pull per Axis', validators=[MinValueValidator(0)])
    recommended_weight = models.FloatField(verbose_name='Recommended weight per Axis',
                                           validators=[MinValueValidator(0)])
    min_work_temp = models.IntegerField(verbose_name='Minimal working temperature')
    max_work_temp = models.IntegerField(verbose_name='Maximum working temperature')
    combo_weight = models.IntegerField(verbose_name='Combo weight', validators=[MinValueValidator(0)])
    waterproof = models.TextField(verbose_name='Waterproof')
    rated_power = models.IntegerField(verbose_name='Rated power', validators=[MinValueValidator(0)])
    starter_length = models.IntegerField(verbose_name='Starter length', validators=[MinValueValidator(0)])
    starter_width = models.IntegerField(verbose_name='Starter width', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class Pump(models.Model):
    name = models.TextField(verbose_name='Pump')
    min_work_voltage = models.IntegerField(verbose_name='Minimal working voltage', validators=[MinValueValidator(0)])
    max_work_voltage = models.IntegerField(verbose_name='Maximum working voltage', validators=[MinValueValidator(0)])
    consumption = models.IntegerField(verbose_name='Consumption', validators=[MinValueValidator(0)])
    weight = models.IntegerField(verbose_name='Weight', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class UAV(models.Model):
    name = models.TextField(verbose_name='Unmanned aerial vehicle')
    serial_id = models.TextField(verbose_name='Serial Id', default='0')
    description = models.TextField(verbose_name='Description', max_length=255)
    deployed_length = models.IntegerField(verbose_name='Deployed length', validators=[MinValueValidator(0)])
    deployed_width = models.IntegerField(verbose_name='Deployed width', validators=[MinValueValidator(0)])
    deployed_height = models.IntegerField(verbose_name='Deployed height', validators=[MinValueValidator(0)])
    rolled_up_length = models.IntegerField(verbose_name='Rolled up length', validators=[MinValueValidator(0)])
    rolled_up_width = models.IntegerField(verbose_name='Rolled up width', validators=[MinValueValidator(0)])
    rolled_up_height = models.IntegerField(verbose_name='Rolled up height', validators=[MinValueValidator(0)])
    weight = models.IntegerField(verbose_name='Weight', validators=[MinValueValidator(0)])
    max_weight = models.IntegerField(verbose_name='Max Weight', validators=[MinValueValidator(0)])
    speed = models.IntegerField(verbose_name='Speed', validators=[MinValueValidator(0)])
    max_speed = models.IntegerField(verbose_name='Max speed', validators=[MinValueValidator(0)])
    flight_time_full = models.IntegerField(verbose_name='Flight time with full tank',
                                           validators=[MinValueValidator(0)])
    flight_time_empty = models.IntegerField(verbose_name='Flight time with empty tank',
                                            validators=[MinValueValidator(0)])
    area_per_flight = models.IntegerField(verbose_name='Area per 1 flight', validators=[MinValueValidator(0)])
    area_per_hour = models.IntegerField(verbose_name='Area per 1 hour', validators=[MinValueValidator(0)])
    tank = models.IntegerField(verbose_name='Tank', validators=[MinValueValidator(0)])
    drop_size = models.IntegerField(verbose_name='Drop size', validators=[MinValueValidator(0)])
    price = models.IntegerField(verbose_name='Price')
    status = models.TextField(verbose_name='Status')


class Parts(models.Model):
    charger = models.ForeignKey(Charger, on_delete=models.CASCADE)
    remote_control = models.ForeignKey(RemoteControl, on_delete=models.CASCADE)
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    propeller = models.ForeignKey(Propeller, on_delete=models.CASCADE)
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    nozzles = models.ForeignKey(Nozzles, on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE)
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.TextField(verbose_name='Article', default='№')
    contract_date = models.DateField(verbose_name='Contract date')
    document = models.URLField(verbose_name='Document')


class Request(models.Model):
    request_type = models.TextField(verbose_name='Request type', default='None')
    request_goal = models.TextField(verbose_name='Request Goal', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    status = models.TextField(verbose_name='Status', max_length=15)


class SimpleRequest(models.Model):
    request_goal = models.TextField(verbose_name='Request Goal', max_length=255)


class TechService(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)


class Repairing(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    parts = models.ForeignKey(Parts, on_delete=models.CASCADE)


class PartReplace(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    parts = models.ForeignKey(Parts, on_delete=models.CASCADE)


class ElectronicCard(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    document = models.URLField(verbose_name='Document')


class Notification(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(verbose_name='DateTime Notice')
    notice = models.TextField(verbose_name='Notice', max_length=250)








