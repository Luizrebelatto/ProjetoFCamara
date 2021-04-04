from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser, Profile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        is_donor = self.cleaned_data.get('is_donor')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')

        if not is_donor:
            raise forms.ValidationError('Usuario não é Doador')

        return super(UserLoginForm, self).clean(*args, **kwargs)


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
