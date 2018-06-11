from django.urls                  import path
from rest_framework.urlpatterns   import format_suffix_patterns
from .views                       import ProjectView

urlpatterns = [
    path('all', ProjectView.all),
    path('get/<int:id>', ProjectView.get),
    path('create', ProjectView.create),
    path('update/<int:id>', ProjectView.update),
    path('destroy/<int:id>', ProjectView.destroy),
]
