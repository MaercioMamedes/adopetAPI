from rest_framework import serializers
from django.contrib.auth.models import User
from core.helpers import validate_name, validate_password



class TutorSerializer(serializers.Serializer):
    
    fullname = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=50)
    password_confirm = serializers.CharField(max_length=50)

    def validate(self, attrs):
        
        fullname = attrs['fullname']
        email = attrs['email']
        password = attrs['password']
        password_confirm = attrs['password_confirm']

        if not validate_name(fullname):
            raise serializers.ValidationError({'fullname':'O campo nome não pode conter número'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'Já existe um usuário cadastrado com esse email'})
 
        if password != password_confirm:
            raise serializers.ValidationError({'password':'Senhas diferentes'})
        
        if not validate_password(password):
            raise serializers.ValidationError({'password': 'A senha não pode conter espaços em branco"'})
        
        return attrs
