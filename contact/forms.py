from django import forms
from .models import Contact


class ContactForm(forms.Form):
    """ Form to send message to admin """
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea, max_length=1000)
