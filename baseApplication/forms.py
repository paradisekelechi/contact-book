from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email',)
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)