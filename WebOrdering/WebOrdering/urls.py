from django.conf.urls import patterns, include, url
from WebOrdering.home_view import *
from WebOrdering.about_view import *
from WebOrdering.register_view import *
from WebOrdering.old_customer_view import *
from WebOrdering.new_customer_view import *
from WebOrdering.result_view import *
from WebOrdering.submit_view import *
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
    url(r'^about/$',about),
	url(r'^login/admin/$',admin),
    url(r'^(.*).js$',js_resource),
    url(r'^(.*).css$',css_resource),
    url(r'^(.*).gif$',gif_resource),
    url(r'^(.*).png$',png_resource),
    url(r'^(.*).jpg$',jpg_resource),
)
