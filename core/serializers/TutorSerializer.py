from rest_framework import serializers
from django.contrib.auth.models import User


class TutorSerializer(serializers.Serializer):
    
    fullname = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=50)
    password_confirm = serializers.CharField(max_length=50)

