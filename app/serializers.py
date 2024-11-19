from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer  

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)   # ase ajobebs clinetsidestvis 
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_by']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'description', 'created_by']  # Add other fields if necessary
        read_only_fields = ['created_by']  # Prevent users from setting this directly

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['created_by'] = request.user  # Automatically set created_by to the logged-in user
        return super().create(validated_data)

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'