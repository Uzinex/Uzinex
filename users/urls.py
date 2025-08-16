from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPIView, MeAPIView, ProfileUpdateAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('me/', MeAPIView.as_view()),
    path('me/profile/', ProfileUpdateAPIView.as_view()),
]
