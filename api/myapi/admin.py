from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=('id','race','gender','created_At')
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','age','father_name','gender')
@admin.register(Worker)
class PersonAdmin(admin.ModelAdmin):
    list_display=('id','name','age','race')