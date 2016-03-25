# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,ListView,CreateView, UpdateView
from django.views.generic import DetailView, DeleteView
from contacts.models import Contact, Group
from django.core.urlresolvers import reverse
import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

def hello_world(reqquest):
    return HttpResponse("hello, world")
    
class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)
        
class ContactOwnerMixin(object):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )
        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied
        return obj
        
class MyView(View):
    def get(self, reqquest, *args, **kwargs):
        return HttpResponse("Hello, World")

class ContactView(LoggedInMixin, DetailView):
    model = Contact
    template_name = 'contact.html'
    
	
class ListContactView(LoggedInMixin, ListView):
    model = Contact
    template_name = 'contact_list.html'
    

class CreateContactView(LoggedInMixin,CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
	return reverse('contacts-list')

    def get_context_data(self, **kwargs):
	context = super(CreateContactView, self).get_context_data(**kwargs)
	context['action'] = reverse('contacts-new')
	return context

class UpdateContactView(UpdateView):
	model = Contact
	template_name = 'edit_contact.html'
	form_class = forms.ContactForm

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

class EditContactAddressView(UpdateView):
    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet
    
    def get_success_url(self):
        return self.get_object().get_absolute_url()
        

