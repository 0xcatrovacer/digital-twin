from django.contrib import admin

# Register your models here.

from .models import Data, Field, Sensor

admin.site.register(Data)

admin.site.register(Field)

admin.site.register(Sensor)
