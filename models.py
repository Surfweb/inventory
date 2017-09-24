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
    
    def __str__(self):
	    return self.hostname
	    
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
	    