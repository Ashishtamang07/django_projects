from django.shortcuts import render
from .models import Profile, Post, Song, User

# Create your views here.

def home(request):
    return render(request,"account/home.html" )
    
def show_user_data(request):
    data1= User.objects.all()
    # data2= User.objects.filter(email='tamangashish314@gmailcom')
    data2= User.objects.filter(email='sabina@gmailcom')
    print(data2)
    "model__modelattribute"
    data3= User.objects.filter(profile__profile_bio= 'teacher')
    "here mypost is related_name to Post model "
    data4= User.objects.filter(mypost__post_title= "travelling")
    data5= User.objects.filter(song__song_duration= 2)
    return render(request, "account/user.html", {'data1':data1, 'data2':data2, 'data3':data3, "data4":data4, "data5":data5})
