from django.urls import path
from .views import HomeView, DoacoesView, SobreView, SejaDoadorView, PontosColetaView, FacaDoacoesView, PontosDoacaoView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('receba-doacoes/', DoacoesView.as_view(), name='receba-doacoes'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('seja-doador/', SejaDoadorView.as_view(), name='seja-doador'),
    path('pontos-coleta/', PontosColetaView.as_view(), name='pontos-coleta'),
    path('accounts/faca-doacoes/', FacaDoacoesView.as_view(), name='faca-doacoes'),
    path('accounts/pontos-doacao/', PontosDoacaoView.as_view(), name='pontos-doacao'),

]
