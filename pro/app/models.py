from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.IntegerField()

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.IntegerField()
    salary = models.IntegerField()
    bonus = models.IntegerField()

    class Meta:
        ordering = ['-id']


    
