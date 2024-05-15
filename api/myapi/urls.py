from api.urls import path
from . views import *

urlpatterns = [
    path('', get_data),
    path('post-data', post_student)
]