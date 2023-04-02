from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from core.models import TutorProfile


class TutorRetrieveView(RetrieveAPIView):

    def get_queryset(self):
        return TutorProfile.objects.get(pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):

        tutor = self.get_queryset()

        return Response(
            {
                "fullname": tutor.fullname,
                "email": tutor.user.email,
                "phone": tutor.phone,
                "city": tutor.city,
                "about":tutor.about,
            }
        )
