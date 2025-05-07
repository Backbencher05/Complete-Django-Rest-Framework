from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError("Only alphanumeric characters are allowed")


class CarList(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    # let apply validation
    # field level validation
    chachisnumber = models.CharField(max_length=100,blank=True,validators=[])
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True,null=True)