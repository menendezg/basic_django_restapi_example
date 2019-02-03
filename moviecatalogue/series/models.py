from django.db import models

# Create your models here.


class Serie(models.Model):
    """Serie class model representation."""
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'HORROR'),
        (COMEDY, 'COMEDY'),
        (ACTION, 'ACTION'),
        (DRAMA, 'DRAMA'),
    )
    
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
