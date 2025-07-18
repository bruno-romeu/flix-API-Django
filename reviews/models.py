from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        #validador para garantir que o número de estrelas esteja entre 1 e 5
        validators=[
        MinValueValidator(0, 'Avaliação não pode ser menor que 0'),
        MaxValueValidator(5, 'Avaliação não pode ser maior que 5')
    ])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie.title