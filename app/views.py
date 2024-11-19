from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsOwnerOrReadOnly  # Custom permission

class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  

    def create(self, request, *args, **kwargs):
        data = request.data
        
        project = Project.objects.create(
            name=data['name'],
            description=data['description'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            created_by=request.user
        )

        project.save()
        serializer = self.get_serializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        if project.created_by != request.user:
            return Response({'detail': 'You do not have permission to edit this project.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        if project.created_by != request.user:
            return Response({'detail': 'You do not have permission to delete this project.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.created_by != request.user and task.project.created_by != request.user:
            return Response({'detail': 'You do not have permission to edit this task.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        if task.created_by != request.user and task.project.created_by != request.user:
            return Response({'detail': 'You do not have permission to delete this task.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class TaskStatusView(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(responsible_person=self.request.user)
from django.shortcuts import get_object_or_404

class TimerView(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        # Override to handle retrieval by project ID
        timer = get_object_or_404(self.queryset, project=pk)
        serializer = self.get_serializer(timer)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def switch_responsibility(self, request, pk=None):
        timer = self.get_object()
        new_responsible_id = request.data.get('new_responsible')

        try:
            new_responsible = User.objects.get(id=new_responsible_id)
            timer.current_responsible = new_responsible
            timer.save()  # Save the updated timer
            return Response({'message': 'Responsibility switched successfully.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view

    def perform_create(self, serializer):
        serializer.save()
        
# class QuestionView(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [IsAuthenticated]
#     # def perform_create(self, serializer):
#     #     project_id = self.kwargs.get('project_id')  # Capture project ID from URL
#     #     project = generics.get_object_or_404(Project, id=project_id)
#     #     serializer.save(project=project)