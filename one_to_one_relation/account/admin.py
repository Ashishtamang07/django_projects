from django.contrib import admin
from .models import Page

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display= ["page_number","page_publish_date","user"]

