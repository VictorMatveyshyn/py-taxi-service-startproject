from django.contrib import admin

# Register your models here.
from taxi.models import Manufacturer, Driver, Car

admin.site.register(Manufacturer)
admin.site.register(Driver)
admin.site.register(Car)



