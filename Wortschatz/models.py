from django.db import models

class Artikel(models.Model):
    bezeichnung = models.CharField(max_length=256, verbose_name='Artikel')
    plural = models.BooleanField(verbose_name='plural')

class Substantiv(models.Model):
    bezeichnung = models.CharField(max_length=256, verbose_name='Substantiv')
    artikel = models.ForeignKey(Artikel, null=False, blank=False, on_delete=models.PROTECT, verbose_name='Artikel')

