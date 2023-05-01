from django.urls import path, include
from rest_framework import routers
from core.views import TutorUserCreateView, TutorListView, TutorUpdateView, TutorRetrieveView, TutorDestroyView, \
    TutorViewSet


router = routers.DefaultRouter()
router.register('tutores', TutorViewSet, basename='tutores')

