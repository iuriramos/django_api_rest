from django.conf.urls             import url
from rest_framework.urlpatterns   import format_suffix_patterns
from .views                       import ProjectView

urlpatterns = [
    url(r'^all/', ProjectView.all),
    url(r'^get/(?P<id>\d+)/', ProjectView.get),
    url(r'^create/', ProjectView.create),
    url(r'^update/(?P<id>\d+)/', ProjectView.update),
    url(r'^destroy/(?P<id>\d+)/', ProjectView.destroy),
]
