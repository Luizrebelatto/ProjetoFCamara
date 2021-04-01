from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Atualizado em')
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ListaMaterial(Base):
    lista_nome = models.CharField(max_length=50, verbose_name='Nome da Lista')

    def __str__(self):
        return self.lista_nome

    class Meta:
        verbose_name = 'Lista de Material'
        verbose_name_plural = 'Lista de Materiais'


class Material(Base):
    item_nome = models.CharField(max_length=50, verbose_name='Nome Item')
    item_quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    lista_material = models.ForeignKey(ListaMaterial, on_delete=models.CASCADE,
                                       verbose_name='Lista de Materiais', blank=True, null=True)

    def __str__(self):
        return self.item_nome

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'


class Relative(Base):
    relative_name = models.CharField(max_length=50, verbose_name='Nome Completo')
    relative_birth = models.DateField(max_length=10, verbose_name='Data de Nascimento')
    relative_grade = models.CharField(max_length=10, verbose_name='Ciclo/Série')
    relative_school = models.CharField(max_length=50, verbose_name='Escola')
    relative_parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                        verbose_name='Responsavel', blank=False, null=False)
    relative_material = models.ForeignKey(ListaMaterial, on_delete=models.CASCADE,
                                          verbose_name='Lista de Materiais', blank=True, null=True)

    def __str__(self):
        return self.relative_name

    class Meta:
        verbose_name = 'Dependente'
        verbose_name_plural = 'Dependentes'


class PontosColeta(Base):
    ponto_nome = models.CharField(max_length=50, verbose_name='Nome')
    ponto_endereco = models.CharField(max_length=80, verbose_name='Endereço')
    ponto_numero = models.PositiveIntegerField(verbose_name='Numero')
    ponto_bairro = models.CharField(max_length=30, verbose_name='Bairro')
    ponto_tipo = models.CharField(max_length=20, verbose_name='Tipo')
    ponto_uf = models.CharField(
        max_length=2,
        verbose_name='Estado',
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    relative_parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                        verbose_name='Responsavel', blank=False, null=False)

    def __str__(self):
        return self.ponto_nome

    class Meta:
        verbose_name = 'Ponto de Coleta'
        verbose_name_plural = 'Pontos de Coleta'