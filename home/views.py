from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages


def index(request):
    form = NewsletterForm
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
