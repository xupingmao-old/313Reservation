from django.conf.urls import patterns, include, url
from WebOrdering.user_views import *
from WebOrdering.food_views import *
from WebOrdering.order_views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebOrdering.views.home', name='home'),
    # url(r'^WebOrdering/', include('WebOrdering.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
