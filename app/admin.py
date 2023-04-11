from django.contrib import admin
from .models import Feedback
# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    '''Admin View for Feedback'''
    list_display = ('name', 'email', 'rating', 'message')