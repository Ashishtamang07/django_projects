from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            "valid data can be access by cleaned_data.get() after validation"
            username= form.cleaned_data.get('username')
            messages.success(request, 'your account has been created? now you can Log In ')
            return redirect('login')
    else:
        form =UserRegisterForm()
    return render(request, 'users/register.html', {"form":form})

"""
profile templates, cant access profile url without login,
instance= request.user shows the current user login while updating ,
instance= request.user.profile.image shows the current user profile image,

"""
@login_required
def profile(request):
    if request.method == 'POST':
        user_form= UserUpdateForm(request.POST, instance=request.user)
        profile_form= ProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'your account has been updated')
            return redirect('profile')
    else:
        user_form= UserUpdateForm(instance=request.user)
        profile_form= ProfileUpdateForm(instance= request.user.profile)
    # user_form= UserUpdateForm(instance=request.user)
    # profile_form= ProfileUpdateForm(instance=request.user.profile)
    
    context={
        'user_form': user_form,
        'profile_form': profile_form

    }
    
    return render(request, 'users/profile.html', context)
    
