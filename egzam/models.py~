# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError
# Create your models here.


class Sala(models.Model):
    nazwa = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.nazwa
    
    class Meta:
        verbose_name_plural="Sale"
    
class Profesor(models.Model):
    nazwisko = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.nazwisko
        
    class Meta:
        verbose_name_plural="Profesorzy"

class Egzamin(models.Model):
    STATUS_CHOICES = (
        ('JZ', 'jeszcze nie zaczął'),
        ('PR', 'trwa'),
        ('SK', 'skończony'),
    )
    WYNIK_CHOICES = (
	('2', '2'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True, null=True)
    idStudenta = models.IntegerField(unique=True)
    idEgzaminatora = models.ForeignKey(Profesor,blank=True, null=True, on_delete=models.SET_NULL)
    sala = models.ForeignKey(Sala, blank=True, null=True, on_delete=models.SET_NULL)
    wynik = models.CharField(max_length=3, null=True, blank=True, choices=WYNIK_CHOICES) 

    class Meta:
        verbose_name_plural="Egzaminy"
        
    def __unicode__(self):
        return "Egzamin nr " + str(self.id)
    
    def clean(self):
      # Don't allow draft entries to have a pub_date.
      if self.status == 'PR':
	  for e in Egzamin.objects.filter(idEgzaminatora=self.idEgzaminatora):
	    if e.status == 'PR':
	      raise ValidationError('Ten Profesor juz prowadzi egzamin.')
	  for e in Egzamin.objects.filter(status='PR'):
	    if e.sala == self.sala:
	      raise ValidationError('W tej sali trwa egzamin')
      # Set the pub_date for published items if it hasn't been set already.
      if (self.status == 'PR' or self.status == 'SK') and self.sala is None:
	  raise ValidationError('Musisz podac salę.')
        
    
class EgzaminEditor(admin.ModelAdmin):
    fields = ['status', 'idEgzaminatora', 'idStudenta', 'sala', 'wynik']
  
admin.site.register(Sala)
admin.site.register(Profesor)
admin.site.register(Egzamin, EgzaminEditor)