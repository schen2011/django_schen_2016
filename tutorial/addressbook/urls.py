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

    url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(),
        name='contacts-edit',),

    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),
        name='contacts-delete',),
                       
    url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),
        name='contacts-view',),

    url(r'^group$', contacts.views.ListGroupView.as_view(),
    name='groups-list',),

    url(r'^newgroup$', contacts.views.CreateGroupView.as_view(),
    name='groups-new',),

    url(r'^editgroup/(?P<pk>\d+)/$', contacts.views.UpdateGroupView.as_view(),
    name='groups-edit',),
)

urlpatterns += staticfiles_urlpatterns()
