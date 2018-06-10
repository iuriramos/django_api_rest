# posts/serializers.py
from rest_framework import serializers
from .models        import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = Project
