from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm


def index(request):
    return render(request, 'home/index.html', {})


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
