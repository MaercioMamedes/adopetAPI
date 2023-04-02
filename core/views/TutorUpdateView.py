from rest_framework.generics import UpdateAPIView
from core.serializers import TutorUpdateSerializer
from core.models import TutorProfile
from rest_framework.response import Response


class TutorUpdateView(UpdateAPIView):
    serializer_class = TutorUpdateSerializer

    def get_queryset(self):
        return TutorProfile.objects.get(pk=self.kwargs['pk'])
    

    def patch(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        print(self.kwargs['pk'])

        if serializer.is_valid(raise_exception=True):

            tutor = self.get_queryset()

            for attr in serializer.validated_data.key():

                
                """data = {
                    'fullname': serializer.validated_data['fullname'],
                    'email': serializer.validated_data['email'],
                    'phone': serializer.validated_data['phone'],
                    'city': serializer.validated_data['city'],
                    'about': serializer.validated_data['about'],
                }"""

            return Response('data')
    
    
    def put(self, request, *args, **kwargs):


        return super().put(request, *args, **kwargs)

    def _update_tutor(tutor, data):
        if 'fullname' in data.keys():
            tutor.fullname = data['fullname']
            tutor.save()
