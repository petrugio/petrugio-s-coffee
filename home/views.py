from django.shortcuts import render
from testimonials.models import Testimonials


def index(request):
    """ A view to return the index page """
    queryset = Testimonials.objects.filter(
        status=1).order_by("-created")[:3]
    return render(
        request,
        'home/index.html',
        {
            'testimonials': queryset,
        }
    )
