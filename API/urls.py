from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', views.getUsers),
    path('users/<str:pk>/', views.getUser),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add-complaint/', views.addComplaint),
    path('against/', views.getAgainst),
    path('reviewer/', views.getReview),
]
