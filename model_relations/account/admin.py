from django.contrib import admin
from .models import Profile, Post, Song
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    "here user is id as primary key "
    list_display= ["profile_bio", "created_at","user"]
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    "here user is id as primary key "
    list_display= ["id","post_title", "user"]
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    "here user is id as primary key "
    list_display= ["id","song_title", "song_duration","singer"]

