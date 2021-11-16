from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering =  ['created']
    
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published= models.DateTimeField(verbose_name='Fecha de publicación', default=datetime.now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Posteo'
        verbose_name_plural = 'Posteos'
        ordering =  ['created']
    
    def __str__(self) -> str:
        return self.title
