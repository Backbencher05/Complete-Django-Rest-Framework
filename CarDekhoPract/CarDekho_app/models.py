from django.db import models

# Create your models here.

class CarModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length = 70)
    active = models.BooleanField(default=False)
    # let apply somevalidations
    # field level validation 
    chachisnumber = models.CharField(max_length=70,blank=True,null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)

