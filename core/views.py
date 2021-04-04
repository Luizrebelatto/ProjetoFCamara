from django.shortcuts import render
from django.views.generic import TemplateView


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


class PontosDoacaoView(TemplateView):
    template_name = 'core/pontodoacao.html'


class FacaDoacoesView(TemplateView):
    template_name = 'core/facadoacoes.html'


class DoadorListaView(TemplateView):
    template_name = 'core/listamateriaisdoador.html'