# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,ListView,CreateView, UpdateView
from django.views.generic import DetailView, DeleteView
from contacts.models import Contact, Group
from django.core.urlresolvers import reverse

def hello_world(reqquest):
	return HttpResponse("hello, world")

class MyView(View):
	def get(self, reqquest, *args, **kwargs):
		return HttpResponse("Hello, World")

class ContactView(DetailView):
    model = Contact
    template_name = 'contact.html'
	
class ListContactView(ListView):
	model = Contact
	template_name = 'contact_list.html'

class CreateContactView(CreateView):
	model = Contact
	template_name = 'edit_contact.html'

	def get_success_url(self):
		return reverse('contacts-list')

	def get_context_data(self, **kwargs):
		context = super(CreateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contacts-new')
		return context

class UpdateContactView(UpdateView):
	model = Contact
	template_name = 'edit_contact.html'

	def get_success_url(self):
		return reverse('contacts-list')

	def get_context_data(self, **kwargs):
		context = super(UpdateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contacts-edit', kwargs={'pk': self.get_object().id})
		return context

class DeleteContactView(DeleteView):
	model = Contact
	template_name = 'delete_contact.html'

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

	def get_context_data(self):
		context = super(CreateGroupView, self).get_context_data(**kwargs)
		context['action'] = reverse('groups-new')
		return context

class UpdateGroupView(UpdateView):
	model = Group
	template_name = 'edit_group.html'

	def get_success_url(self):
		return reverse('groups-list')

	def get_context_data(self, **kwargs):
		context = super(UpdateGroupView, self).get_context_data(**kwargs)
		context['action'] = reverse('groups-edit', kwargs={'pk': self.get_object().id})
		return context

