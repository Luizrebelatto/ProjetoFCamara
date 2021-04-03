from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import TemplateView, CreateView, UpdateView


class HomeView(TemplateView):
    template_name = 'core/index.html'


class DoacoesView(TemplateView):
    template_name = 'core/doacoes.html'


class SobreView(TemplateView):
    template_name = 'core/sobre.html'


class SejaDoadorView(TemplateView):
    template_name = 'core/sejadoador.html'


class PontosColetaView(TemplateView):
    template_name = 'core/pontoscoleta.html'




