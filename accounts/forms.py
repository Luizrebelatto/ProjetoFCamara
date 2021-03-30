from django import forms
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput

from .models import CustomUser, Profile


class CustomUserCreateForm(UserCreationForm, forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
        ]
        labels = {'username': 'Usuário'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.username = self.cleaned_data['email']
        user.is_cliente = True

        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


class ProfileChangeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['fone', 'adress', 'adress_number', 'city', 'uf', 'imagem']
