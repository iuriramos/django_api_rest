# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
