# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,ListView,CreateView
from contacts.models import Contact, Group
from django.core.urlresolvers import reverse

def hello_world(reqquest):
	return HttpResponse("hello, world")

class MyView(View):
	def get(self, reqquest, *args, **kwargs):
		return HttpResponse("Hello, World")

class ListContactView(ListView):
	model = Contact
	template_name = 'contact_list.html'

class CreateContactView(CreateView):
	model = Contact
	template_name = 'edit_contact.html'

	def get_success_url(self):
		return reverse('contacts-list')


class ListGroupView(ListView):
	model = Group
	template_name = 'group_list.html'

class CreateGroupView(CreateView):
	model = Group
	template_name = 'edit_group.html'

	def get_success_url(self):
		return reverse('groups-list')