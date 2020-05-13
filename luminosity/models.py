from django.db import models

# Create your models here.

from django.db import models
import uuid

class Luminosity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='tipo', max_length=20)
    value = models.IntegerField(verbose_name='valor')
    latitude = models.IntegerField(verbose_name='latitud_del_lugar', null=True, blank=True)
    length = models.IntegerField(verbose_name='longitud_del_lugar', null=True, blank=True)
    terrain = models.CharField(verbose_name='tipo_de_terreno', max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)