from django.urls import path
from core.views import TutorUserCreateView, TutorListView, TutorUpdateView


urlpatterns = [
    path('cadastro', TutorUserCreateView.as_view(), name='register'),
    path('tutores', TutorListView.as_view(), name='tutors'),
    path('tutores/<int:pk>', TutorUpdateView.as_view(), name='tutor_update')
]

