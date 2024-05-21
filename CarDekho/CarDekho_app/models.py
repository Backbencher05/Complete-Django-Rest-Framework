from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def alphanumaric(value):
    if not str(value).isalnum():
        raise ValidationError('Only alphanumaric Character are allowed')

class CarList(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    # let apply validation
    # field level validation
    chachisnumber = models.CharField(max_length=100,blank=True,null=True, validators=[alphanumaric])
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
