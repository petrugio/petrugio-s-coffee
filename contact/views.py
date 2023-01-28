from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages


def contact(request):
    """ Send a message to site owner/admin """
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            if request.user.is_authenticated:
                user = request.user
            else:
                user = None

            # Save the message to the database
            contact = Contact(
                name=name,
                email=email,
                message=message,
                user=user)

            contact.save()
            messages.success(request, 'Successfully send message!')
            # Redirect to the 'contact' page
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'Failed to send message.'
                'Please ensure the form is valid.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
