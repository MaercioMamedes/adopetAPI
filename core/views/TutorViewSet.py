from rest_framework import viewsets
from core.models import TutorProfile
from core.serializers import TutorSerializer, TutorUpdateSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class TutorViewSet(viewsets.ViewSet):

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    def get_object(self, pk):
        return get_object_or_404(TutorProfile, pk=pk)

    def list(self, request):
        """Método para listar todos os objetos Tutores cadastrados"""

        queryset = TutorProfile.objects.all()
    
        # Formatação da lista de tutores
        tutor_list = [

            {   
                'id_tutor': tutor.id,
                'fullname': tutor.fullname,
                'email': tutor.user.email,
                'phone': tutor.phone,
                'city': tutor.city,

                } for tutor in queryset
                
                ]
        
        return Response(tutor_list)

    def create(self, request):
        """Método para criar um novo Tutor"""

        serializer_data = TutorSerializer(data=request.data)

        if serializer_data.is_valid(raise_exception=True):

            fullname = serializer_data.validated_data['fullname']
            email = serializer_data.validated_data['email']
            password = serializer_data.validated_data['password']

            """Criando usuário para aplicação"""

            user = User.objects.create_user(
                first_name = fullname.split()[0],
                last_name = fullname.split()[-1],
                username=email,
                email=email,
            )

            user.set_password(password)
            user.save()

            """Criando perfil de Tutor"""

            tutor = TutorProfile.objects.create(
                user=user,
                fullname=fullname,
            )

            return Response({
                'fullname': tutor.fullname,
                'email':tutor.user.email,
            },
            status=201)

    def retrieve(self, request, pk=None):
        """Método para recuperar um tutor a partir do id"""
        
        tutor = self.get_object(pk)
                
        return Response(
            {
                "id_tutor": tutor.id,
                "fullname": tutor.fullname,
                "email": tutor.user.email,
                "phone": tutor.phone,
                "city": tutor.city,
                "about":tutor.about,
            }
        )

    def update(self, request, pk=None):
        """Método HTTP para atualização total de recursos"""

        serializer =TutorUpdateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            tutor = self.get_object(pk)

            data = {}
            
            serializers_fields = (
                'fullname',
                'email',
                'phone',
                'city',
                'about'
            )

            for field in serializers_fields:
                if field not in serializer.validated_data.keys():
                    return Response('Dados incompletos, para atualização parcial utilize o método PATCH', status=400)
            

            for attr in serializer.validated_data.keys():

                data[attr] = serializer.validated_data[attr]

            self._update_tutor(tutor, data)

            return Response('dados atualizados com sucesso')

    def partial_update(self, request, pk=None):
        """Método HTTP para atualização parcial de recurso"""

        serializer = TutorUpdateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            tutor = self.get_object(pk)
            data = {}

            for attr in serializer.validated_data.keys():
                data[attr] = serializer.validated_data[attr]
                
            self._update_tutor(tutor, data)

            return Response('dados atualizados com sucesso')

    def destroy(self, request, pk=None):
        """Método para excluir um tutor"""

        tutor = self.get_object(pk)
        tutor.user.delete()
        tutor.delete()
        return Response('Usuário excluído com sucesso')
    
    
    def _update_tutor(self, tutor, data):

            """Atualização do tutor"""

            if 'fullname' in data.keys():
                tutor.fullname = data['fullname']
                tutor.user.fisr_name = data['fullname'][0]
                tutor.user.last_name = data['fullname'][-1]
                tutor.user.save()
                tutor.save()

            if 'email' in data.keys():
                tutor.user.email = data['email']
                tutor.user.username = data['email']
                tutor.user.save()
                tutor.save()

            if 'phone' in data.keys():
                tutor.phone = data['phone']
                tutor.save()
            
            if 'city' in data.keys():
                tutor.city = data['city']
                tutor.save()

            if 'about' in data.keys():
                tutor.about = data['about']
                tutor.save()
            
            return tutor
        