import uuid

from django.db import models

class Planet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name='Nome', null=False)
    chemical_elements = models.CharField(max_length=200, verbose_name='Elementos químicos')
    percentage_of_water = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Porcentagem de água')
    alphaR_distance = models.PositiveIntegerField(verbose_name='Distância até alphaR em km')
    probability_of_life = models.CharField(max_length=20, choices=(
        ('Incerta', 'Incerta'),
        ('Provável', 'Provável'),
        ('Improvável', 'Improvável')
    ), verbose_name='Probabilidade de vida')
