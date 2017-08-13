from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Nodes(models.Model):
    ip = models.CharField(max_length=300)
    hostname = models.CharField(max_length=300)
    region = models.CharField(max_length=300)
    sity = models.CharField(max_length=300)
    site = models.CharField(max_length=1500)
    description = models.TextField()
    
    def __str__(self):
        return "<tr><td>"+self.ip + "</td><td>" + self.hostname + "</td><td>" + self.region + "</td><td>" + self.sity + "</td><td>" + self.description + "</td><tr>"