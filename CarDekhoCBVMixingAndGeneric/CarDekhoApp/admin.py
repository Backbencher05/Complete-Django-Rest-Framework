from django.contrib import admin
from CarDekhoApp.models import *
# Register your models here.

class ShowroomListAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'website']

class CarListAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active', 'chachisnumber', 'price']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating', 'comments', 'car', 'created', 'updated']

    
admin.site.register(ShowroomList,ShowroomListAdmin)
admin.site.register(CarList,CarListAdmin)
admin.site.register(Review, ReviewAdmin)