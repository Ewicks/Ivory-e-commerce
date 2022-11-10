from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    All fields from the Contact model will be displayed in the ContactForm
    """
    class Meta:
        model = Contact
        fields = "__all__"
