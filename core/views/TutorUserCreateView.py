from core.serializers import TutorSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from core.models import TutorProfile


class TutorUserCreateView(CreateAPIView):
    """View para criar usuário da aplicação"""
    
    serializer_class = TutorSerializer


    def post(self, request, *args, **kwargs):

        serializer_data = self.get_serializer(data=request.data)

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
        