# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


	    

# Список стран присутствия		
@python_2_unicode_compatible
class Country(models.Model):
	#code = models.CharField(max_length=300, blank=True)
	name = models.CharField(max_length=300)
	name_local = models.CharField(max_length=300, blank=True)
	iflag = models.FileField(blank=True)
	def __str__(self):
		return self.name
	    
# Список регионов / штатов присутствия	
@python_2_unicode_compatible
class Region(models.Model):
	#code = models.CharField(max_length=300, blank=True)
	name = models.CharField(max_length=300, blank=True)
	name_local = models.CharField(max_length=300, blank=True)
	origin = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
	    return self.name_local
	
# Список городов
@python_2_unicode_compatible
class Sity(models.Model):
	#code = models.CharField(max_length=300, blank=True)
	name = models.CharField(max_length=300, blank=True)
	name_local = models.CharField(max_length=300, blank=True)
	origin = models.ForeignKey(Region, on_delete=models.CASCADE)
	def __str__(self):
		return self.name_local

	
# Список площадок
@python_2_unicode_compatible
class Site(models.Model):
	#code = models.CharField(max_length=300)
	name = models.CharField(max_length=300, blank=True)
	name_local = models.CharField(max_length=300, blank=True)
	origin = models.ForeignKey(Sity, on_delete=models.CASCADE)
	def __str__(self):
	    return self.name
       
   	#class Meta:
    #    verbose_name = u"Площадка"
    #    verbose_name_plural = u"Площадка"
	
# БД автономных систем
#class As_db(models.Model):
#	as_number = models.CharField(max_length=300)

#class Ipv4(models.Model):
#	as_number = models.CharField(max_length=300)	# Номер AS оригинатора
#	address_family = models.CharField(max_length=300)	# ipv4, vpnv4
#	network = models.CharField(max_length=300) # Выделенный префикс
#	description = models.TextField()	# Описание сети
#	
#	    def __str__(self):
#	    return self.network

# Добавить address_family / VRF поле
@python_2_unicode_compatible
class Nodes(models.Model):
    ip = models.CharField(max_length=300)
    hostname = models.CharField(max_length=300)
    #country = models.ForeignKey(Country, on_delete=models.CASCADE)
    #region = models.CharField(max_length=300, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    #sity = models.CharField(max_length=300, blank=True)
    sity = models.ForeignKey(Sity, on_delete=models.CASCADE)
    site = models.CharField(max_length=1500, blank=True)
    description = models.TextField(blank=True)
	#neighbors = ...
    
    def __str__(self):
	    return self.hostname

