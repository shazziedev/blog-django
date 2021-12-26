from django.contrib import admin
from .models import *


@admin.register(Article)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'intro', 'stamp')
    list_filter = ( 'author', 'cat', 'active','l_updated','title')
    search_fields = ('title', 'intro', 'body')



@admin.register(Category)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'l_updated' )
    list_filter = ('title', 'l_updated')
    search_fields = ('title', 'l_updated')


@admin.register(Profile)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('phone', 'About',  'l_updated')
    list_filter = ('phone', 'l_updated')
    search_fields = ('phone', 'l_updated', 'About')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')