from django.shortcuts import render
from baseApplication.models import Contact
from .forms import ContactForm
from django.shortcuts import redirect
# Create your views here.


def home(request):
    return render(
        request,
        'baseApplication/home.html',
        {'contactCount': Contact.objects.count()}
    )


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(
        request,
        'baseApplication/add-contact.html',
        {'form': form}
    )

def list_contact(request):
    allContacts = Contact.objects.all()
    return render(
        request,
        'baseApplication/list-contact.html',
        {
            'contacts': allContacts
        }
    )