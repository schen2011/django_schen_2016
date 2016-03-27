from django.contrib import admin
from .models import Contact, Group

class ChoiceInLine(admin.TabularInline):
    model  = Contact
    extra = 1
    
admin.site.register(Group)
admin.site.register(Contact)