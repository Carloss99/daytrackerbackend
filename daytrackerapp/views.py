from django.shortcuts import render
from .models import Task
from rest_framework import viewsets, permissions
from .serializer import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_class = [permissions.AllowAny]