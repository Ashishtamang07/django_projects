from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Images

# Create your views here.

def home(request):
    if request.method == 'POST':
        form= ImageForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        # return redirect('/')
    form = ImageForm()
    img= Images.objects.all()
    
    return render(request, 'myapp/index.html',{'img':img, 'form':form})
def delete(request):
        return render(request, 'myapp/index.html')