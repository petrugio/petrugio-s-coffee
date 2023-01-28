from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ To show messages on the admin page """

    list_display = ('name', 'email', 'date_sent', 'user')
    search_fields = ['title', 'message']
    list_filter = ('email', 'date_sent')


admin.site.register(Contact, ContactAdmin)
