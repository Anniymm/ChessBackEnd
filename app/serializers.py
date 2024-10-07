from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer  

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)  
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_by']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'