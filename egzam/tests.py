"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
    def test_poprawnosci_egzaminow(self):
	for self_e in Egzamin.objects.all():
	    if self_e.status == 'PR':
	      for e in Egzamin.objects.filter(idEgzaminatora=self_e.idEgzaminatora):
		if e.status == 'PR':
		  #raise ValidationError('Profesor prowadzi dwa egzaminy.')
		  assert False
	      for e in Egzamin.objects.filter(status='PR'):
		if e.sala == self_e.sala:
		  assert False
		  #raise ValidationError('Dwa egzaminy w jednej sali')
	    if (self_e.status == 'PR' or self_e.status == 'SK') and self_e.sala is None:
		#raise ValidationError('Trwa lub zakonczony egzamin bez przypisanej sali')
		assert False
        
    def test_unikalnosci_nazw(self):   
        for s in Sala.objects.all():
	  for s2 in Sala.objects.all():
	      if s == s2:
		assert False
        for p in Profesor.objects.all():
	  for p2 in Profesor.objects.all():
	      if p == p2:
		assert False
        
        
        
       