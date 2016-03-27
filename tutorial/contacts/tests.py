"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from contacts.models import Contact
from contacts.views import ListContactView
from django.test.client import Client
from django.test.client import RequestFactory


class ContactTest(TestCase):
    def test_str(self):
        contact = Contact(first_name='John', last_name='Smith')
        self.assertEqual(str(contact),'John Smith')

class ContactListViewTests(TestCase):
    """Contact list view tests."""
    def test_contacts_in_the_context(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(list(response.context['object_list']), [])
        Contact.objects.create(first_name='foo', last_name='bar')
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_contacts_in_the_context_request_factory(self):
        factory = RequestFactory()
        request = factory.get('/')
        response = ListContactView.as_view()(request)
        self.assertEquals(list(response.context_data['object_list']), [])
        Contact.objects.create(first_name='foo', last_name='bar')
        response = ListContactView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)