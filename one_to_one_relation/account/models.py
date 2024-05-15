from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    "if user is deleted, page aslo get deletecreated by user"
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # "u cant delete user if on_delete=models.PROTECT "
    # user= models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    "page can be created by only user, if user is staff, not by normal user"
    # user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})
    page_number= models.CharField(max_length=10)
    page_publish_date= models.DateField()
    
    
    
    


