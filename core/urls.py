from core.views import TutorUserCreateView, TutorListView
from django.urls import path



urlpatterns = [
    path('cadastro', TutorUserCreateView.as_view(), name='register'),
    path('tutores', TutorListView.as_view(), name='tutors')
]

