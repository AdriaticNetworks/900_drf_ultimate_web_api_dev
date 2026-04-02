from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Movie(models.Model):
    class Meta:
            unique_together = ('title', 'country', 'release_year') # This means that there cannot be two Movie entries with the same title, country, and release_year

    title = models.CharField(max_length=255)
    genres = models.JSONField(default=list)
    country = models.CharField(max_length=100, blank=True, null=True)
    extra_data = models.JSONField(default=dict)
    release_year = models.IntegerField(
    validators = [
        MinValueValidator(1888),
        MaxValueValidator(datetime.datetime.now().year)],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
        