from django.contrib import admin
from sensor.models import sensorReading , pressureSensor
# Register your models here.



class SensorAdmin(admin.ModelAdmin):
    pass
class pressureSensorAdmin(admin.ModelAdmin):
    pass
admin.site.register(sensorReading, SensorAdmin)
admin.site.register(pressureSensor, pressureSensorAdmin)