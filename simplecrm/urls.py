from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url':'/static/img/favicon.ico'}),
    url(r'^$', 'customers.views.index', name='home'),
    url(r'^companies$', 'customers.views.companies', name='companies'),
    url(r'^companies/new$', 'customers.views.company_new', name='company_new'),
    url(r'^companies/(?P<company_id>(\d)+)$', 'customers.views.company_view', name='company'),
    url(r'^people$', 'customers.views.people', name='people'),
    url(r'^people/new$', 'customers.views.new_people', name='new_people'),
    url(r'^people/(?P<person_id>(\d)+)$', 'customers.views.person', name='person'),
    # url(r'^simplecrm/', include('simplecrm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
