from core.views import TutorUserCreateView
from django.urls import path



urlpatterns = [
    path('cadastro', TutorUserCreateView.as_view(), name='register')
]

