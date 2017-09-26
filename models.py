# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Добавить address_family / VRF поле
@python_2_unicode_compatible
class Nodes(models.Model):
    ip = models.CharField(max_length=300)
    hostname = models.CharField(max_length=300)
    region = models.CharField(max_length=300)
    sity = models.CharField(max_length=300)
    site = models.CharField(max_length=1500)
    description = models.TextField()
	#neighbors = ...
    
    def __str__(self):
	    return self.hostname

# Список стран присутствия		
class Country(models.Model):
	code = models.CharField(max_length=300)
	name = models.CharField(max_length=300)
	
# Список регионов / штатов присутствия		
class Region(models.Model):
	code = models.CharField(max_length=300)
	name = models.CharField(max_length=300)
	#origin = # Нужен выподающий список из class Country
	
# Список городов
class Sity(models.Model):
	code = models.CharField(max_length=300)
	name = models.CharField(max_length=300)
	#origin_country = # Нужен выподающий список из class Region
	#origin_region = # Нужен выподающий список из class Region с фильтром по origin_country
	
# Список площадок
class Site(models.Model):
	code = models.CharField(max_length=300)
	name = models.CharField(max_length=300)
	#origin_country = # Нужен выподающий список из class Region
	#origin_region = # Нужен выподающий список из class Region с фильтром по origin_country
	#origin_sity = # Выподающий список из class Sity с фильтром по origin_region
	
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
	    