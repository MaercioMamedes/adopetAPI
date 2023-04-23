from rest_framework.generics import DestroyAPIView
from core.models import TutorProfile
from rest_framework.response import Response


class TutorDestroyView(DestroyAPIView):

    def get_queryset(self):
        
        return TutorProfile.objects.get(pk=self.kwargs['pk'])

    def destroy(self, request, *args, **kwargs):
        user_tutor = self.get_queryset().user
        self.perform_destroy(user_tutor)
        return Response('usuário deletado com sucesso')
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)