from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"one user can have inly one profile"
class Profile(models.Model):
    user= models.OneToOneField( User, on_delete=models.CASCADE, primary_key=True)
    profile_bio= models.CharField(max_length=150)
    created_at= models.DateField()
"multiple post can be created by one user"
class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="mypost")
    post_title= models.CharField(max_length=100)
    
"manytomany, one song can sang by multiple singer"
class Song(models.Model):
    user= models.ManyToManyField(User)
    song_title= models.CharField(max_length=50)
    song_duration= models.IntegerField()
    
    def singer(self):
        return",".join([ str(p) for p in self.user.all()])