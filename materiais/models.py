from django.db import models
from django.utils import timezone
from accounts.models import CustomUser, Dependente

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Atualizado em')
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ListaMaterial(Base):

    nome = models.ForeignKey(CustomUser, verbose_name='Nome', on_delete=models.CASCADE)
    dependente = models.ForeignKey(Dependente, verbose_name='Dependente', on_delete=models.CASCADE, blank=True, null=True)
    lapis = models.PositiveIntegerField(default=0, verbose_name='Lápis')
    caderno = models.PositiveIntegerField(default=0, verbose_name='Caderno')
    canetas = models.PositiveIntegerField(default=0, verbose_name='Canetas')
    borracha = models.PositiveIntegerField(default=0, verbose_name='Borracha')
    lapis_cor = models.PositiveIntegerField(default=0, verbose_name='Lápis de Cor')
    tesoura = models.PositiveIntegerField(default=0, verbose_name='Tesoura')
    mochila = models.PositiveIntegerField(default=0, verbose_name='Mochila')

    def __str__(self):
        return self.nome.email

    class Meta:
        verbose_name = 'Lista de Material'
        verbose_name_plural = 'Lista de Materiais'

