from django.shortcuts import render
from rest_framework  import viewsets
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated

class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

