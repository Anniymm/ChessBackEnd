from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'project', ProjectView, basename='projects')
router.register(r'tasks', TaskView, basename='tasks')
router.register(r'taskStatus', TaskStatusView, basename='status')
router.register(r'timer', TimerView, basename='timer')

urlpatterns = [
    path('', include(router.urls)),
]
