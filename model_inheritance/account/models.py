from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    "if user is deleted, page aslo get deletecreated by user"
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  
    page_number= models.CharField(max_length=10)
    page_publish_date= models.DateField()
    
    
"""
when we inherit models it automatically create one to one relation with parent class
but when we inherit model and but dont want to create onetoone relation as it automactically create,
rather we want ontoone with other model we use parent_link= True after providing Parent as first args
"""
class LikePage(Page):
    page_refrence= models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True, parent_link= True)
    like= models.IntegerField()
    
    
    
    


