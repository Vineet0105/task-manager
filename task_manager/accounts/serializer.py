from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()


    def create(self, validated_data):
        if User.objects.filter(username=validated_data['username']).exists():
            return ValidationError("Username already Exists")
    
        user = User.objects.create(username=validated_data['username'],
                            email = validated_data['email']
                            )
        user.set_password(validated_data['password'])
        user.save()

        return validated_data