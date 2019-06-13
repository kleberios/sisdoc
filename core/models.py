from django.db import models

# Create your models here.


class Setor(models.Model):
    nome = models.CharField(max_length=40, verbose_name='Nome do Setor')
    sigla = models.CharField(max_length=10, verbose_name='Sigla do Setor')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Setores'


class Equipamento(models.Model):

    nome = models.CharField(max_length=20, verbose_name='Tipo do equipamento')
    local = models.ForeignKey(Setor, on_delete=models.PROTECT, verbose_name='Localização')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Equipamentos'

class Ativo(models.Model):
    tipo = models.ForeignKey(Equipamento, on_delete=models.PROTECT, verbose_name= 'Tipo de Equipamento')
    local = models.ForeignKey(Setor, on_delete=models.PROTECT, verbose_name= 'Localização')
    ip = models.CharField(max_length=18, verbose_name='Número do IP')
    serial = models.CharField(max_length=20, verbose_name='Serial', null=True, blank=True)
    fabricante = models.CharField(max_length=20, verbose_name='Fabricante')
    modelo = models.CharField(max_length=20, verbose_name='Modelo')
    numportas = models.IntegerField(verbose_name='Número de Portas')
    mac = models.CharField(max_length=17, verbose_name='Número do MAC')
    login = models.CharField(max_length=20, verbose_name='Login')
    senha = models.CharField(max_length=30, verbose_name='Senha')

    def __str__(self):
        return self.tipo.nome

    class Meta:
        verbose_name_plural = 'Ativos'

class Porta(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.PROTECT, verbose_name='Tipo de Ativo')
    porta = models.IntegerField(primary_key=True, verbose_name='Número de Porta')
    idvlan = models.CharField(max_length=10, verbose_name='ID da vlan')
    vlan = models.CharField(max_length=15, verbose_name='Nome da vlan')
    tag = models.CharField(max_length=20, verbose_name='Vlan TAG')
    idponto = models.CharField(max_length=20, null=True, blank=True, verbose_name='ID ponto')

    def __str__(self):
        return self.porta

    class Meta:
        verbose_name_plural = 'Portas'

