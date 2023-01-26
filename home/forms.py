from django import forms
from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    """
    All fields from the Contact model will be displayed in the ContactForm
    """
    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(forms.ModelForm):
    """
    All fields from the Contact model will be displayed in the ContactForm
    """
    class Meta:
        model = Newsletter
        fields = "__all__"
