from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
	
    def __str__(self):
	return ' '.join([self.first_name,self.last_name])
    def get_absulte_url(self, **kwargs):
        return reverse('contacts-view', kwargs={'pk':self.id})

class Group(models.Model):
    group_name = models.CharField(max_length=255)
    member_number = models.IntegerField()

    def __str__(self):
	return self.group_name
	
class Address(models.Model):
    contact = models.ForeignKey(Contact)
    address_type = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=20)
    
    class Meta:
        unique_together = ('contact', 'address_type')