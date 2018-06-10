"""django_api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url('admin/', admin.site.urls),
    url('docs/', include_docs_urls(title='API REST Documents', description='RESTful API Docuementation')),
    url('projects/', include('projects.urls')),
]