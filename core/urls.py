from django.urls import path
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('lista/cadastrar', TesteView.as_view(), name='cadastrar-lista'),
]