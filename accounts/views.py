from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    CreateView,
    UpdateView,
    TemplateView,
)
from .forms import (
    CustomUserCreateForm,
    CustomUserChangeForm,
    ProfileChangeForm,
)
from .models import CustomUser

# Create your views here.


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'accounts/index.html'
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        messages.success(self.request, f'Conta Criada com Sucesso!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possivel Criar a Conta')
        return super(UserCreateView, self).form_invalid(form)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'