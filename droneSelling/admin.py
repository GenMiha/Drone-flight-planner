from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class DroneTypeAdmin(admin.ModelAdmin):
    pass


class TechCardAdmin(admin.ModelAdmin):
    pass


class TechOperationAdmin(admin.ModelAdmin):
    pass


admin.site.register(DroneType, DroneTypeAdmin)
admin.site.register(TechCard, TechCardAdmin)
admin.site.register(TechOperation, TechOperationAdmin)
