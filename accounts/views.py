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
    UserForm,
    CustomUserChangeForm,
    ProfileChangeForm,
    DonorUserForm
)
from .models import CustomUser, Dependente

# Create your views here.


class CadastroView(TemplateView):
    template_name = 'accounts/index.html'


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'accounts/beneficiario.html'
    success_url = reverse_lazy('beneficiario')

    def form_valid(self, form):
        messages.success(self.request, f'Conta Criada com Sucesso!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possivel Criar a Conta')
        return super(UserCreateView, self).form_invalid(form)


class DonorCreateView(CreateView):
    model = CustomUser
    form_class = DonorUserForm
    template_name = 'accounts/beneficiario.html'
    success_url = reverse_lazy('donatario')

    def form_valid(self, form):
        messages.success(self.request, f'Conta Criada com Sucesso!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possivel Criar a Conta')
        return super(DonorCreateView, self).form_invalid(form)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    second_form_class = ProfileChangeForm
    template_name = 'accounts/_profile.html'
    success_url = reverse_lazy('profile')

    def post(self, request, *args, **kwargs):
        form = CustomUserChangeForm(request.POST, instance=request.user)
        form2 = ProfileChangeForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, f'Perfil Atualizado com Sucesso!')
            return redirect('profile')
        else:
            form = CustomUserChangeForm(instance=request.user)
            form2 = ProfileChangeForm(instance=request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.request.user.profile)
        return context

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, f'Perfil Atualizado com Sucesso!!')
        return super(UserUpdateView, self).form_valid(form, *args, **kwargs)

    def test_func(self):
        customuser = self.get_object()
        if self.request.user.pk == customuser.pk:
            return True

        return False


class DependenteCreateView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'accounts/beneficiario.html'
    success_url = reverse_lazy('donatario')

    def form_valid(self, form):
        messages.success(self.request, f'Conta Criada com Sucesso!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possivel Criar a Conta')
        return super(DependenteCreateView, self).form_invalid(form)


class MinhasDoacoesView(TemplateView):
    template_name = 'accounts/doadordoacoes.html'


class MinhasSolicitacoesView(TemplateView):
    template_name = 'accounts/solicitacao.html'


class CadastrarListaView(TemplateView):
    template_name = 'accounts/cadastrarlista.html'