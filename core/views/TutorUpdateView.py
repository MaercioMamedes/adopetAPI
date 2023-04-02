from rest_framework.generics import UpdateAPIView
from core.serializers import TutorUpdateSerializer
from core.models import TutorProfile
from rest_framework.response import Response


class TutorUpdateView(UpdateAPIView):
    serializer_class = TutorUpdateSerializer

    def get_queryset(self):
        return TutorProfile.objects.get(pk=self.kwargs['pk'])
    

    def patch(self, request, *args, **kwargs):

        """Método HTTP para atualização parcial de recurso"""

        serializer = self.get_serializer(data=request.data)


        if serializer.is_valid(raise_exception=True):

            tutor = self.get_queryset()
            data = {}

            for attr in serializer.validated_data.keys():

                data[attr] = serializer.validated_data[attr]
                
            self._update_tutor(tutor, data)

            return Response('dados atualizados com sucesso')
    
    
    def put(self, request, *args, **kwargs):
        """Método HTTP para atualização total de recursos"""
        serializer = self.get_serializer(data=request.data)


        if serializer.is_valid(raise_exception=True):

            tutor = self.get_queryset()
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

  
    

    
    def _update_tutor(self, tutor, data):

        """Atualização parcial do usuário"""

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