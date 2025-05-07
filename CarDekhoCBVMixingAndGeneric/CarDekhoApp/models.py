from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

def alphanumaric(value):
    if not str(value).isalnum():
        raise ValidationError('Only alphanumaric Character are allowed')

class ShowroomList(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    website = models.URLField(max_length=70)

    def __str__(self):
        return self.name
    
class CarList(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=90)
    active = models.BooleanField(default=False)
    chachisnumber =models.CharField(max_length=50,blank=True, null=True,validators=[alphanumaric])
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    showroom = models.ForeignKey(ShowroomList,on_delete=models.CASCADE, related_name = "showrooms", null =True)
    def __str__(self):
        return self.name
    
class Review(models.Model):
    rating = models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comments = models.CharField(max_length=200,null=True)
    car = models.ForeignKey(CarList,on_delete=models.CASCADE, null=True, related_name="Review")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "The rating of" + self.car.name + ":--" + str(self.rating)