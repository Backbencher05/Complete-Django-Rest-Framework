from django.contrib import admin
from CarDekho_app.models import CarList

# Register your models here.
class CarListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'active', 'chachisnumber', 'price']


admin.site.register(CarList, CarListAdmin)