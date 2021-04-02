from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import TemplateView, CreateView, UpdateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'core/index.html'


'''class TesteView(CreateView):
    template_name = 'core/teste.html'
    model = ListaMaterial
    form_class = ListaForm

    def form_valid(self, form):
        form.instance.relative = self.request.user
        return super().form_valid(form)'''