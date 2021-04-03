from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import UpdateView, CreateView, ListView
from accounts.models import Dependente
from django.contrib import messages
from django.urls import reverse_lazy
from accounts.models import Dependente
from .models import ListaMaterial
from .forms import FormMaterial
# Create your views here.


class ListaCreate(CreateView, ListView):
    model = ListaMaterial
    form_class = FormMaterial
    template_name = 'materiais/materiais.html'
    success_url = reverse_lazy('lista-material')
    queryset = ListaMaterial.objects.all()
    context_object_name = 'materiais'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.nome = self.request.user
        messages.success(self.request, f'Lista criada com Sucesso!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Lista já criada!!')
        return super(ListaCreate, self).form_invalid(form)


