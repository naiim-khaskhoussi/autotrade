from django.contrib import admin
from vehicles.models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(FuelType)
admin.site.register(Vehicle)