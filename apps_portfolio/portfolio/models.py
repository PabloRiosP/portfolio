from decimal import Decimal
from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Skill_Type (models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Tipo de Habilidad'
        verbose_name_plural = 'Tipos de Habilidad'

class Skill (models.Model):
    type_skill = models.ManyToManyField(Skill_Type)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
    picture = models.ImageField(upload_to='portfolio/pictures/', verbose_name='Imagen', null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

class Credential_Type (models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Tipo de Credencial'
        verbose_name_plural = 'Tipos de Credencial'

class Credential (models.Model):
    type_credential = models.ManyToManyField(Credential_Type)
    name = models.CharField(verbose_name='Nombre', max_length=50)
    dateEarned = models.DateField(verbose_name='Fecha de obtención', default=now)
    dateExpiration = models.DateField(verbose_name='Fecha de expiración', blank=True, null=True)
    description = models.TextField(verbose_name='Descripción', default="", blank=True, null=True)
    picture = models.ImageField(upload_to='portfolio/pictures/', verbose_name='Imagen', null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    skills = models.ManyToManyField(Skill)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Credencial'
        verbose_name_plural = 'Credenciales'

class Project (models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    date = models.DateField(verbose_name='Fecha', default=now)
    description = models.TextField(verbose_name='Descripción', default="", blank=True, null=True)
    picture = models.ImageField(upload_to='portfolio/pictures/', verbose_name='Imagen', null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    skills = models.ManyToManyField(Skill)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-date']
