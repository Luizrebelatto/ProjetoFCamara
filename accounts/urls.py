from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    UserCreateView,
    UserProfileView
)


urlpatterns = [
    path('cadastro/', UserCreateView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]