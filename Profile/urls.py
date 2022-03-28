from django.urls import path
from . import views


urlpatterns = [
    path('my-account/', views.userAccount, name='my-account'),
    path('<str:pk>/', views.userProfile, name='profile'),
]
