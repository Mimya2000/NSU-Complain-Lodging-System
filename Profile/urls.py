from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk>/', views.userProfile, name='profile'),
]
