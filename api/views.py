from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import ProjectSerializer
from projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]