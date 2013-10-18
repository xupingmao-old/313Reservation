from django.conf.urls import patterns, include, url
from WebOrdering.home_view import *
from WebOrdering.customer_view import *
from WebOrdering.admin_view import *

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
    url(r'^$',home),
    url(r'^choose_food/$',choose_food),
    url(r'^about/$',about),
	url(r'^login/admin/$',admin_login),
    url(r'^admin/(.*)$',admin_manage),
    url(r'^submit/$',submit),
    url(r'^check_submit/$',check_submit),
    url(r'^new_customer/$',new_customer),
    url(r'^old_customer/$',old_customer),
    # check old old_customer or new_customer
    url(r'^check_phone/$',check_phone),
    url(r'^(.*).js$',js_resource),
    url(r'^(.*).css$',css_resource),
    url(r'^(.*).gif$',gif_resource),
    url(r'^(.*).png$',png_resource),
    url(r'^(.*).jpg$',jpg_resource),
)
