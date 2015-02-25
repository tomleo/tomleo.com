from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^posts/(?P<pk>[0-9]+)/(?P<slug>\w+)/$', views.PostDetailView.as_view(), name='post')
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
#TODO: add i18n_patterns
#urlpatterns = i18n_patterns(urlpatterns)

