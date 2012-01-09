# coding: utf-8

from django.db import models

class Cliente(models.Model):
    fone = models.CharField(max_length=16, db_index=True)
    ramal = models.CharField(max_length=4, blank=True, db_index=True)
    contato = models.CharField(max_length=64, db_index=True)
    outros_contatos = models.TextField(blank=True)
    logradouro = models.CharField(max_length=32)
    numero = models.PositiveIntegerField(u'número')
    complemento = models.CharField(max_length=32, blank=True)
    obs = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['fone', 'ramal']
        verbose_name = u'Freguês'
        verbose_name_plural = u'Fregueses'

    def __unicode__(self):
        return u'%s: %s' % (self.fone, self.contato)

    def endereco(self):
        end = '%s, %s' % (self.logradouro, self.numero)
        if self.complemento:
            end += ', ' + self.complemento
        return end
    endereco.short_description = u'endereço'
