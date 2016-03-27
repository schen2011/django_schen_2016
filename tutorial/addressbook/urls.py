from django.conf.urls import patterns, include, url
import contacts.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', contacts.views.ListContactView.as_view(),
    name='contacts-list',),

    url(r'^new$', contacts.views.CreateContactView.as_view(),
    name='contacts-new',),

    url(r'^group$', contacts.views.ListGroupView.as_view(),
    name='groups-list',),

    url(r'^new2$', contacts.views.CreateGroupView.as_view(),
    name='groups-new',),
)

urlpatterns += staticfiles_urlpatterns()
