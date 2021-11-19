from django.db import models

# Create your models here.

from django.utils import timezone

#The information related to the car
class car_info(models.Model):

    #The brand (using letters)
    brand = models.CharField(max_length=50)

    #The consumption(a number)
    consommation = models.DecimalField(default=0, decimal_places=1, max_digits=3)
    def __str__(self):
        
        #When I call an object, the brand is going to show
        return self.brand
