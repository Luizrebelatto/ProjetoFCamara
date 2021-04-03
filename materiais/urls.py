from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ListaCreate,

)

urlpatterns = [
    path('', ListaCreate.as_view(), name='lista-material'),
    #path('', ListaListView.as_view(), name='material'),
]