from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           ps=fm.cleaned_data['password']
           reg= User(name=nm, email=em, password=ps)
           reg.save()
           fm= StudentRegistration()
           
           
    else:
        fm= StudentRegistration()
    student = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm, 'student':student})


def update(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk =id)        
        fm= StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= User.objects.get(pk =id)
        fm= StudentRegistration( instance=pi)
   
    return render(request, 'enroll/updatestudent.html',{'form':fm})

def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk= id)
        pi.delete()
        return redirect( '/')
    

