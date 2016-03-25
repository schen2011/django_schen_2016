from django.db import models
from django.core.urlresolvers import reverse

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