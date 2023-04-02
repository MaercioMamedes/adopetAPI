from rest_framework import serializers
from django.contrib.auth.models import User


class TutorUpdateSerializer(serializers.Serializer):
    
    fullname = serializers.CharField(max_length=50, required=False)
    email = serializers.EmailField(max_length=100, required=False)
    phone = serializers.CharField(max_length=13, required=False)
    city = serializers.CharField(max_length=50, required=False)
    about = serializers.CharField(required=False)


