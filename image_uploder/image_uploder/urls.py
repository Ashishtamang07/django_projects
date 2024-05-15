
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#its urlpattern thats find the mediafiles 
# print(static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT))
