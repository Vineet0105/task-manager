from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "Message": "User already Registered\nPlease Login",                  
            },status.HTTP_201_CREATED)
        serializer.save()
        return Response({
            "Message": "User Registered\nPlease Login to get acces code",                  
        },status.HTTP_201_CREATED)