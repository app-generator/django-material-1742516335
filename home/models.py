# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Atracao(models.Model):

    #__Atracao_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    horario_funcionamento = models.TextField(max_length=255, null=True, blank=True)
    idade_minima = models.IntegerField(null=True, blank=True)

    #__Atracao_FIELDS__END

    class Meta:
        verbose_name        = _("Atracao")
        verbose_name_plural = _("Atracao")


class Avaliacao(models.Model):

    #__Avaliacao_FIELDS__
    usuario = models.CharField(max_length=255, null=True, blank=True)
    nota = models.IntegerField(null=True, blank=True)
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Avaliacao_FIELDS__END

    class Meta:
        verbose_name        = _("Avaliacao")
        verbose_name_plural = _("Avaliacao")


class Comentario(models.Model):

    #__Comentario_FIELDS__
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    aprovado = models.BooleanField()

    #__Comentario_FIELDS__END

    class Meta:
        verbose_name        = _("Comentario")
        verbose_name_plural = _("Comentario")


class Endereco(models.Model):

    #__Endereco_FIELDS__
    linha2 = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    #__Endereco_FIELDS__END

    class Meta:
        verbose_name        = _("Endereco")
        verbose_name_plural = _("Endereco")


class Pontoturistico(models.Model):

    #__Pontoturistico_FIELDS__
    descricao = models.TextField(max_length=255, null=True, blank=True)
    aprovado = models.BooleanField()
    atracoes = models.ForeignKey(Atracao, on_delete=models.CASCADE)
    comentarios = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    avaliacoes = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    #__Pontoturistico_FIELDS__END

    class Meta:
        verbose_name        = _("Pontoturistico")
        verbose_name_plural = _("Pontoturistico")



#__MODELS__END
