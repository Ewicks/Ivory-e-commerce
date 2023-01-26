from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def index(request):
    form = NewsletterForm
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have subscribed')
            return redirect('home')
    #  """Send the user a confirmation email"""
    cust_email = 'LOL'
    subject = render_to_string(
        'home/confirmation_emails/newsletter_email_subject.txt')
    body = render_to_string(
        'home/confirmation_emails/newsletter_email_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    return render(request, 'home/index.html', {'form': form})


def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully')
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
