
from django.contrib import admin
from django.urls import path, include
from .views import (UserRegistrationView,
                    UserLoginView,
                    UserProfileView,
                    UserChangePasswordView,
                    SendPasswordResetEmailView, 
                    UserPasswordRestView)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name= 'register'),
    path('login/', UserLoginView.as_view(), name= 'login'),
    path('profile/', UserProfileView.as_view(), name= 'profile'),
    path('change-password/', UserChangePasswordView.as_view(), name= 'change_password'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name= 'send_reset_password_email'),
    path('reset-password/<uid>/<token>/', UserPasswordRestView.as_view(), name= 'reset_password'),
    
  
]
