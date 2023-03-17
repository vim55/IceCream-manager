from django.db import models

# Create your models here.
# data type ref:
# https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/
class Store(models.Model):
    # null info is not allowed
    name = models.CharField(max_length=60) # maximum length set to 60
    location = models.CharField(max_length=200) # maximum length set to 200
    contact_email = models.EmailField(max_length=100) # predefined regex which checks '@'
    
class Tub(models.Model):
    # null info is not allowed
    flavour = models.CharField(max_length=30) # maximum length set to 60
    size = models.FloatField() # set to float for litres
    isVegan = models.BooleanField(default = False) # Default is False
    isGlutenFree = models.BooleanField(default = False) # Default is False
    store = models.ForeignKey(Store, on_delete=models.CASCADE) # one store can have many tubs, but not vice-versa