from rest_framework import viewsets
from core.models import TutorProfile
from core.serializers import TutorSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class TutorViewSet(viewsets.ViewSet):

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        return TutorProfile.objects.get(pk=self.kwargs['pk'])
    
    def get_serializer(self, **kwargs):
        return TutorSerializer

    def list(self, request):

        queryset = TutorProfile.objects.all()

        """Formatação da lista de tutores"""

        tutor_list = [
            {
                'fullname': tutor.fullname,
                'email': tutor.user.email,
                'phone': tutor.phone,
                'city': tutor.city,

                } for tutor in queryset
                
                ]
        
        return Response(tutor_list)


    def create(self, request):
            
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
            status=200)

    def retrieve(self, request, pk=None):
        
        tutor = TutorProfile.objects.get(pk=pk)
                
        return Response(
            {
                "fullname": tutor.fullname,
                "email": tutor.user.email,
                "phone": tutor.phone,
                "city": tutor.city,
                "about":tutor.about,
            }
        )

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        print("passsou aqui")

        tutor = TutorProfile.objects.get(pk=pk)

        tutor.user.delete()
        tutor.delete()
        print('pronto')

        
        return Response('foir')