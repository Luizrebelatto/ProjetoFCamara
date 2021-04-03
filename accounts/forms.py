from django import forms
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput

from .models import CustomUser, Profile


class UserForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'cpf',
            'fone',
            'adress',
            'adress_number',
            'city',
            'uf',
            'email',
        ]
        labels = {'username': 'Usuário'}

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.username = self.cleaned_data['email']
        user.is_donor = False

        if commit:
            user.save()
        return user


class DonorUserForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'cpf',
            'fone',
            'adress',
            'adress_number',
            'city',
            'uf',
            'email',
        ]
        labels = {'username': 'Usuário'}

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.username = self.cleaned_data['email']
        user.is_donor = True

        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'cpf',
            'fone',
            'adress',
            'adress_number',
            'city',
            'uf'
        ]


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagem']