from django.conf.urls import patterns, url
from blog.views import PostList, PostDetail


urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view()),
)
