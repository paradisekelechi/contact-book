from django.urls import path
from django.conf.urls import url
from .views import home, add_contact, list_contact
urlpatterns = [
    url(r'^add$', add_contact, name='add_contact'),
    url(r'^list$', list_contact, name='list_contacts'),
    url(r'$', home, name='home')
]