from django.forms import ModelForm
from .models import PontosColeta


class FormMaterial(ModelForm):
    class Meta:
        model = PontosColeta
        fields = ('__all__', )