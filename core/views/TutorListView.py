from rest_framework.generics import ListAPIView
from core.models import TutorProfile
from rest_framework.response import Response


class TutorListView(ListAPIView):

    queryset = queryset = TutorProfile.objects.all()

    def list(self, request, *args, **kwargs):


        """Formatação da lista de tutores"""
        tutor_list = [
            {
                'fullname': tutor.fullname,
                'email': tutor.user.email,
                'phone': tutor.phone,
                'city': tutor.city,

                } for tutor in self.get_queryset()
                
                ]
        
        return Response(tutor_list)
    

    """def get_queryset(self):
        return super().get_queryset()"""

    def get(self, request, *args, **kwargs):

        if len(self.get_queryset()) == 0:
            return Response('Não encontrado', status=404)
        
        else:
            return self.list(request, *args, **kwargs)
