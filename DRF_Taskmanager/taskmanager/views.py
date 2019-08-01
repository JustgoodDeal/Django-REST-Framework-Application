from rest_framework import viewsets
from taskmanager.serializers import UsersSerializer, ProjectsSerializer, TasksSerializer
from taskmanager.models import User, Project, Task


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer    
    queryset = User.objects.all()


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer   
    queryset = Project.objects.all()


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer   
    queryset = Task.objects.all()
