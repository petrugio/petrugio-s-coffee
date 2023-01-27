from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testimonials
from checkout.models import Order
from django.contrib.auth.models import User
from .forms import TestimonialForm


def testimonial_list(request):
    """Function to display testimonials
       and to check if the user made any orders"""
    queryset = Testimonials.objects.filter(status=1).order_by("-created")
    user_email = request.user.email if hasattr(request.user, 'email') else ""
    has_orders = Order.objects.filter(
        email=user_email).count() > 0
    paginate_by = 6

    return render(
        request,
        'testimonials/testimonials.html',
        {
            'testimonials': queryset,
            'has_orders': has_orders,
        }
    )


# def testimonial_detail(request, slug):

#     queryset = Testimonials.objects.filter(status=1)
#     testimonial = get_object_or_404(queryset, slug=slug)

#     return render(
#         request,
#         "testimonials/testimonial_detail.html",
#         {
#             "testimonial": testimonial
#         }
#     )


@login_required
def add_testimonial(request):
    """ Add a testimonial to the store website """

    has_orders = Order.objects.filter(
        email=request.user.email).count() > 0

    if request.method == 'POST':
        if has_orders:
            form = TestimonialForm(request.POST)
            if form.is_valid():
                testimonial = form.save(commit=False)
                testimonial.author = request.user
                testimonial.save()
                messages.success(request, 'Successfully added testimonial!')
                return redirect(reverse(
                    'testimonials'))
            else:
                messages.error(
                    request, 'Failed to add testimonial.'
                    'Please ensure the form is valid.')
        else:
            messages.error(
                    request, 'Failed to add testimonial.'
                    'Please oder something before adding a testimonial.')
    else:
        form = TestimonialForm()

    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
