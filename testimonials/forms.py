from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Testimonials

STATUS_CHOICES = ((0, "Draft"), (1, "Published"))


class TestimonialForm(forms.ModelForm):
    """ Form to add a testimonial """

    title = forms.CharField(max_length=254)
    content = forms.CharField(widget=SummernoteWidget(), max_length=1000)
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Testimonials
        fields = ('title', 'content',
                  'status')
