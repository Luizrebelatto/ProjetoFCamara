from django.forms import ModelForm
from .models import ListaMaterial


class FormMaterial(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome')

        if nome:
            self.add_error(
                'nome',
                'Lista ja criada'
            )

    class Meta:
        model = ListaMaterial
        fields = ['lapis', 'caderno', 'canetas', 'borracha', 'lapis_cor', 'tesoura', 'mochila']