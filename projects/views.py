# -*- coding: utf-8 -*-
from __future__                import unicode_literals
from .models                   import Project
from rest_framework.decorators import api_view
from rest_framework.response   import Response
from rest_framework            import status
from .services                 import ProjectService
import json

class ProjectView():

    @api_view(['GET'])
    def all(request):
        result_service = ProjectService.all(Project)
        return Response(result_service, status=status.HTTP_200_OK)


    @api_view(['GET'])
    def get(request, id):
        result_service = ProjectService.get(Project, id)
        return Response(result_service, status=status.HTTP_200_OK)


    @api_view(['POST'])
    def create(request):
        result_service = ProjectService.create(Project, request.body)
        return Response(result_service, status=status.HTTP_201_CREATED)


    @api_view(['PUT'])
    def update(request, id):
        result_service = ProjectService.update(Project, id, request.body)
        return Response(result_service, status=status.HTTP_200_OK)


    @api_view(['DELETE'])
    def destroy(request, id):
        ProjectService.destroy(Project, id)
        return Response(status=status.HTTP_204_NO_CONTENT)
