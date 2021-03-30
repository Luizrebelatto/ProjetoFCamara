from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    UserCreateView,
    UserProfileView,
    DonorCreateView,
)


urlpatterns = [
    path('cadastro/donatario', UserCreateView.as_view(), name='register'),
    path('cadastro/doador', DonorCreateView.as_view(), name='doador'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]