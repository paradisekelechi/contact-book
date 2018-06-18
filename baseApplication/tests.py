from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class PageTests(TestCase):

    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'baseApplication/home.html')
        self.assertContains(response, '<h2>View All Contacts In Your</h2>')

    def test_add_page_view(self):
        response = self.client.get(reverse('add_contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'baseApplication/add-contact.html')
        self.assertContains(response, '<h2>Add New Contact</h2>')

    def test_list_page_view(self):
        response = self.client.get(reverse('list_contacts'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'baseApplication/list-contact.html')
        self.assertContains(response, '<h2>No contacts in your directory</h2>')