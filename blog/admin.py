from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created', 'updated')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
