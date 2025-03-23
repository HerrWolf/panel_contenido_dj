from django.db import models
from core.dashboard.choices import STATE_MOVIE_CHOICES, AUDIO_MOVIE_CHOICES

# Create your models here.
class ContentType(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de contenido'
        verbose_name_plural = 'Tipos de contenido'

class Category(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    tmdb_id = models.IntegerField()
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    backdrop_url = models.URLField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=10, choices=STATE_MOVIE_CHOICES, default='catalogo')
    audio = models.CharField(max_length=20, choices=AUDIO_MOVIE_CHOICES)
    overview = models.TextField(blank=True, null=True)
    release_date = models.CharField(max_length=6, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='movies')
    video_path = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.tmdb_id} | {self.audio}"

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'
        ordering = ['-id']
