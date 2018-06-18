from django.shortcuts import render


# Create your views here.
def home(request):
    return render(
        request,
        'baseApplication/home.html'
    )

def addContact(request):
    return render(
        request,
        'baseApplication/add-contact.html',
    )

def listContact(request):
    return render(
        request,
        'baseApplication/list-contact.html',
    )