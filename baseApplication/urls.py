from django.urls import path
from django.conf.urls import url
from .views import home, addContact, listContact
urlpatterns = [
    url(r'^add$', addContact, name='add_contact'),
    url(r'^list$', listContact, name='list_contacts'),
    url(r'$', home, name='home')
]