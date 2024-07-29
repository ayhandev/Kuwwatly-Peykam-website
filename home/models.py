from django.db import models
from django.utils.translation import gettext_lazy as _

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=255, default="None")

    def __str__(self):
        return self.title

class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"Фото ({self.gallery.title})"