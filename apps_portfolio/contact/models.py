from django.db import models

class Social_Type (models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)

    def __str__ (self):
        return "[{0}] {1}".format(self.id, self.name)

class Social (models.Model):
    type_social = models.ManyToManyField(Social_Type)
    name = models.CharField(verbose_name='Nombre', max_length=30, default='UNNAMED')
    logo = models.ImageField(verbose_name='Logo', upload_to='contact/logos/', null=False)
    url = models.URLField(verbose_name='URL', blank=True, null=True)

    def __str__(self):
        return "[{0}] {1}".format(self.id, self.name)

class Contact (models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre', blank=False, null=False)
    mail = models.EmailField(max_length=255, verbose_name='Correo', blank=False, null=False)
    subject = models.CharField(max_length=100, verbose_name='Asunto', blank=False, null=False)
    message = models.TextField(verbose_name='Mensaje', blank=False, null=False)

    def __str__(self):
        return "[{0}] {1}".format(self.id, self.subject)

