from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views

urlpatterns = [
    # path('projects/index', views.ProjectList.as_view(), name='project-list'),
    # path('projects/<int:id>', views.ProjectDetail.as_view(), name='project-detail'),

    path('/index', views.ProjectList.as_view()),
    path('/<int:pk>', views.PostDetail.as_view()),
]
