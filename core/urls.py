from django.urls import path
from .views import HomeView, DoacoesView, SobreView, SejaDoadorView, PontosColetaView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('receba-doacoes/', DoacoesView.as_view(), name='receba-doacoes'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('seja-doador/', SejaDoadorView.as_view(), name='seja-doador'),
    path('pontos-coleta/', PontosColetaView.as_view(), name='pontos-coleta'),
]
