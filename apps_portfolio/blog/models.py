from django.db import models
from django.utils.timezone import now

class Post (models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    date = models.DateField(verbose_name='Fecha', default=now)
    content = models.TextField(verbose_name='Contenido', default="", blank=True, null=True)
    picture = models.ImageField(upload_to='blog/pictures/', verbose_name='Imagen', null=True)

    def __str__(self):
        return "[{0}] {1}".format(self.id, self.title)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-date']

