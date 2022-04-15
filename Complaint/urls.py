from django.urls import path
from . import views

urlpatterns = [
    path('add-complaint/', views.addComplaint, name='add-complaint'),
    path('complaint-card/<str:pk>/', views.complaintCard, name='complaint-card'),
    path('status/', views.complaintStatus, name='status'),
]