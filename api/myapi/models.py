from django.db import models

# Create your models here.

class BaseClass(models.Model):
    created_At = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Person(BaseClass):
    # name= models.CharField(max_length=100)
    # address= models.CharField(max_length=100)
    race=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    
class Student(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField(default=18)
    father_name= models.CharField(max_length=100)
    gender= models.ForeignKey(Person, on_delete= models.CASCADE , null=True)
    
class Worker(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField(default=18)
    race= models.ForeignKey(Person, on_delete= models.CASCADE)
   
    
