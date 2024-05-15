from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
from django.core.mail import send_mail

def home(request):
 
    send_mail(
    "testing",
    "checking mail",
    "tamangashish314@gmail.com",
    ["ashishtmg2056@gmail.com"],
    fail_silently=False,
)
    return HttpResponse("hello ashish")