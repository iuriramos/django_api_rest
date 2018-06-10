# -*- coding: utf-8 -*-
from __future__                import unicode_literals
from rest_framework            import generics
from .models                   import Project
from .serializers              import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework            import viewsets
from rest_framework.response   import Response
from rest_framework            import status
import json

class ProjectView():
    @api_view(['POST'])
    def create(request):
        queryset = Project.objects.create(**json.loads(request.body))
        serializer = ProjectSerializer(instance=queryset)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def update(request):
        queryset = Project.objects.create(**json.loads(request.body))
        serializer = ProjectSerializer(instance=queryset)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

# class ProjectList(generics.ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class PostDetail(generics.RetrieveAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
