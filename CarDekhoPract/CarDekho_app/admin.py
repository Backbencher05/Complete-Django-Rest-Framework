from django.contrib import admin
from CarDekho_app.models import CarModel
# Register your models here.

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active', 'chachisnumber', 'price']


admin.site.register(CarModel,CarModelAdmin) 
