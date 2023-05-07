from rest_framework import serializers
from django.contrib.auth.models import User
from core.helpers import validate_name, validate_image


class TutorUpdateSerializer(serializers.Serializer):
    
    fullname = serializers.CharField(max_length=50, required=False)
    email = serializers.EmailField(max_length=100, required=False)
    phone = serializers.CharField(max_length=13, required=False)
    city = serializers.CharField(max_length=50, required=False)
    about = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)


    def validate(self, attrs):

        if 'fullname' in attrs.keys():
            fullname = attrs['fullname'] 
            if not validate_name(fullname):
                raise serializers.ValidationError({'fullname':'O campo nome não pode conter número'})
            
        if 'email' in attrs.keys():
            email = attrs['email']
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email':'Já existe um usuário cadastrado com esse email'})
            
        if 'image' in attrs.keys():            
            image = attrs['image']

            if validate_image(image):
                raise serializers.ValidationError({'image':'imagem do perfil só pode ser jpg ou png'})

        

        return attrs