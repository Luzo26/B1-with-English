import email

from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# Modelo para el contacto
class Contact(models.Model):
    email=models.EmailField()
    nombre=models.CharField(max_length=100)
    consulta=models.TextField()
    telefono=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.nombre

#Modelo para apuntarse
class Apuntar(models.Model):
    nombre=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=100)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    curso=models.CharField(max_length=100)
    mes=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.curso


# creating model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Base_posts')
    body=RichTextUploadingField()
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    class Meta:
        ordering = ('-publish',)
        def __str__(self):
           return self.title
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
        return reverse('Base:post_detail',args=[self.slug])