from django.urls import path
from . import views

urlpatterns = [
    path('add-complaint/', views.addComplaint, name='add-complaint'),
]