from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField( max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    
def __str__(self)->str:
    return self.name

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed=models.IntegerField()
    
def __str__(self)->str:
    return self.car_name
