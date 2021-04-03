from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Atualizado em')
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class PontosColeta(Base):
    ponto_nome = models.CharField(max_length=50, verbose_name='Nome do Local')
    ponto_cnpj = models.CharField(max_length=50, verbose_name='CNPJ')
    ponto_razao = models.CharField(max_length=50, verbose_name='Razão Social')
    ponto_cep = models.CharField(max_length=80, verbose_name='CEP')
    ponto_cidade = models.CharField(max_length=80, verbose_name='Cidade')
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
    ponto_bairro = models.CharField(max_length=30, verbose_name='Bairro')
    ponto_endereco = models.CharField(max_length=80, verbose_name='Endereço')
    ponto_numero = models.CharField('Telefone', max_length=15)
    ponto_telefone = models.CharField(max_length=20, verbose_name='Telefone')

    def __str__(self):
        return self.ponto_nome

    class Meta:
        verbose_name = 'Ponto de Coleta'
        verbose_name_plural = 'Pontos de Coleta'
