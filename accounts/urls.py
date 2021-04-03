from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    UserCreateView,
    UserProfileView,
    UserUpdateView,
    CadastroView,
    DonorCreateView,
    MinhasDoacoesView,
    CadastrarListaView,
    MinhasSolicitacoesView
)


urlpatterns = [

    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('cadastro/beneficiario', UserCreateView.as_view(), name='beneficiario'),
    path('cadastro/doador', DonorCreateView.as_view(), name='doador'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/profile/', UserUpdateView.as_view(), name='profile-update'),
    path('cadastrar-lista/', CadastrarListaView.as_view(), name='cadastrar-lista'),
    path('minhas-doacoes/', MinhasDoacoesView.as_view(), name='minhas-doacoes'),
    path('minhas-solicitacoes/', MinhasSolicitacoesView.as_view(), name='minhas-solicitacoes'),
]
