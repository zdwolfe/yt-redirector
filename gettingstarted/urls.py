from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import app.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', app.views.index, name='index'),

)
