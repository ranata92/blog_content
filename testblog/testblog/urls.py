from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    # Examples:
    # url(r'^$', 'testblog.views.home', name='home'),
    # url(r'^testblog/', include('testblog.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
