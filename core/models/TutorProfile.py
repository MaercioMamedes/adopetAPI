from django.db import models
from django.contrib.auth.models import User


class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField('Nome completo', max_length=100)
    phone = models.CharField('telefone', max_length=13)
    city = models.CharField('cidade', max_length=50)
    about = models.TextField('Sobre')
    image = models.ImageField('imagem', upload_to='image_profile', blank=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
