from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='home'),
    path('register/', views.teacher_register, name='register'),
    path('success/', views.success, name='success'),
    path('update/<int:id>/', views.update, name='update'),
]
