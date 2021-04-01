from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    UserCreateView,
    UserProfileView,
    UserUpdateView
)


urlpatterns = [
    path('cadastro/donatario', UserCreateView.as_view(), name='donatario'),
    #path('cadastro/doador', DonorCreateView.as_view(), name='doador'),
    #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/profile/', UserUpdateView.as_view(), name='profile-update'),
]
