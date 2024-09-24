from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskStatusView(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskSerializer

class TimerView(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer

