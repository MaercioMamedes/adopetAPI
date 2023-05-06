from rest_framework import routers
from core.views import TutorViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('tutores', TutorViewSet, basename='tutores')
