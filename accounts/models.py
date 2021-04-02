import uuid
from django.db import models
from django.utils import timezone
from datetime import date
from stdimage.models import StdImageField
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)
from materiais.models import ListaMaterial
from pontocoleta.models import PontosColeta


def get_file_path(_instace, filename) -> str:
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    file_path = f'avatar/{year}/{month}/{day}/'
    ext = filename.split('.')[-1]
    file_name = f'{file_path}{uuid.uuid4()}.{ext}'
    return file_name


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Atualizado em')
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Dependente(Base):
    dependente_nome = models.CharField(max_length=50, verbose_name='Nome Completo')
    dependente_nascimento = models.DateField(max_length=10, verbose_name='Data de Nascimento')
    dependente_serie = models.CharField(max_length=10, verbose_name='Ciclo/Série')
    dependente_escola = models.CharField(max_length=50, verbose_name='Escola')
    dependente_lista = models.ForeignKey(ListaMaterial, on_delete=models.DO_NOTHING, blank=True, null=True)
    ponto_coleta = models.ForeignKey(PontosColeta, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.dependente_nome

    class Meta:
        verbose_name = 'Dependente'
        verbose_name_plural = 'Dependentes'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('O E-mail é Obrigatório')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    is_staff = models.BooleanField('Membro da Equipe', default=False)
    is_donor = models.BooleanField('Doador', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=15)
    fone = models.CharField('Telefone', max_length=15)
    adress = models.CharField(max_length=100, verbose_name='Endereço')
    adress_number = models.CharField(max_length=6, verbose_name='Numero')
    city = models.CharField('Cidade', max_length=30)
    uf = models.CharField(
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
    imagem = StdImageField(upload_to=get_file_path, blank=True, verbose_name='Imagem',
                           variations={'thumb': {'width': 150, 'height': 150, 'crop': True}}, delete_orphans=True)
    dependente = models.ManyToManyField(Dependente)

    def __str__(self):
        return f'{self.user.email} Profile.'

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

