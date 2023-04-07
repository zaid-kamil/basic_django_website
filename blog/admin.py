from django.contrib import admin
from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    '''Admin View for Article'''
    list_display = ('title','slug','created_on')

admin.site.register(Tag)
