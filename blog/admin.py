from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','question','answer','created_at','updated_at','answer_by')
    list_filter = ('name','email','question','answer','created_at','updated_at','answer_by')