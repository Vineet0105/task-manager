from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TaskFilter

class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TaskFilter
    search_fields = ['title', 'description']  # enable ?search=
    ordering_fields = ['due_date', 'priority', 'status']  # enable ?ordering=
    ordering = ['due_date']

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

