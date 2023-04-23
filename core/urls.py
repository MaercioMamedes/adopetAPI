from django.urls import path, include
from rest_framework import routers
from core.views import TutorUserCreateView, TutorListView, TutorUpdateView, TutorRetrieveView, TutorDestroyView, \
    TutorViewSet


router = routers.SimpleRouter()
router.register(r'tutors', TutorViewSet, basename='tutor')

urlpatterns = [
    #path('cadastro', TutorUserCreateView.as_view(), name='register'),
    #path('tutores', TutorListView.as_view(), name='tutors'),
    #path('tutores/<int:pk>', TutorUpdateView.as_view(), name='tutor_update'),
    #path('tutor/<int:pk>', TutorRetrieveView.as_view(), name='tutor_profile'),
    #path('tutores/<int:pk>', TutorDestroyView.as_view(), name='tutor_delete'),
    path('users/',include(router.urls)),

]

