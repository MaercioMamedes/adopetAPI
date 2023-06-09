from django.contrib import admin
from core.models import TutorProfile

# Register your models here.

@admin.register(TutorProfile)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname')
