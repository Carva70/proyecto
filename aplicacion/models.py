from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid  # Required for unique book instances


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=True, name="username")

    class Meta:
        ordering = ['username']

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.username}'

class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=100, null=True, name="texto")
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, name="usuario")
    fecha = models.DateField(name="fecha", null=True)

    class Meta:
        ordering = ['fecha']

    def get_absolute_url(self):
        return reverse('tweet-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.texto}'

class Retweet(models.Model):
    id = models.AutoField(primary_key=True)
    tweet = models.ForeignKey('Tweet', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    fechaDeRetweet = models.DateField(name="fechaDeRetweet", null=True)

    class Meta:
        ordering = ['fechaDeRetweet']

    def get_absolute_url(self):
        return reverse('retweet-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.fechaDeRetweet)

