from django.conf.urls             import url
from django.urls                  import path
from rest_framework.urlpatterns   import format_suffix_patterns
from .views                       import ProjectView

urlpatterns = [
    url('create', ProjectView.create),
]
