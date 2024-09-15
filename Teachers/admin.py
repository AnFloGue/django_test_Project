from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'email', 'phone')
    list_display_links = ('name', 'age', 'gender', 'email', 'phone')