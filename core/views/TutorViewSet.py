from rest_framework import viewsets
from core.models import TutorProfile
from rest_framework.response import Response

class TutorViewSet(viewsets.ViewSet):

    def get_queryset(self):
        return TutorProfile.objects.get(pk=self.kwargs['pk'])

    def list(self, request):

        queryset = queryset = TutorProfile.objects.all()

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
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
