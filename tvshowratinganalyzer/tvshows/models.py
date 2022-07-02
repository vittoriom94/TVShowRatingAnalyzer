from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Show(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.name


class Episode(models.Model):
    title = models.CharField(max_length=255)
    episode = models.IntegerField()
    season = models.IntegerField()
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])

    def __str__(self):
        return f'{self.show.name} - S{self.season:02d}E{self.episode:02d} - {self.title}'


