from django.contrib import admin
from .models import Poll, Choice
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
class HistoryAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    pass
@admin.register(Poll)
class PollAdmin(HistoryAdmin ):
    list_display=["question","pub_date"]
@admin.register(Choice)
class ChoiceAdmin(HistoryAdmin ):
    list_display=["poll", "choice_text", "votes"]
