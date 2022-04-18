from django.urls import path
from . import views


urlpatterns = [
    path('my-account/', views.userAccount, name='my-account'),
    path('update-profile/', views.updateProfile, name='update-profile'),
    path('<str:pk>/', views.userProfile, name='profile'),
]
