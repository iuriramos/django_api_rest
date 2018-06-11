# -*- coding: utf-8 -*-
from __future__                import unicode_literals
from .models                   import Project
from .serializers              import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response   import Response
from rest_framework            import status
from .services                 import ProjectService
import json

class ProjectView():

    @api_view(['GET'])
    def all(request):
        queryset = ProjectService.all(Project)
        serializer = ProjectSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @api_view(['GET'])
    def get(request, id):
        queryset = ProjectService.get(Project, id)
        serializer = ProjectSerializer(instance=queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @api_view(['POST'])
    def create(request):
        queryset = ProjectService.create(Project, request.body)
        serializer = ProjectSerializer(instance=queryset, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @api_view(['PUT'])
    def update(request, id):
        queryset = ProjectService.update(Project, id, request.body)
        serializer = ProjectSerializer(instance=queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @api_view(['DELETE'])
    def destroy(request, id):
        ProjectService.destroy(Project, id)
        return Response(status=status.HTTP_204_NO_CONTENT)
