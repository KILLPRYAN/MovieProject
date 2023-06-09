from email.policy import default

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_mail = models.EmailField()

    def get_url(self):
        return reverse('director_detail', args=[self.id])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        ('M', 'Мужчина'),
        ('F', 'Женщина')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def get_url(self):
        return reverse('actor_detail', args=[self.id])

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актер {self.first_name} {self.last_name}"
        else:
            return f"Актриса {self.first_name} {self.last_name}"


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        ('E', 'Euro'),
        ('D', 'Dollars'),
        ('R', 'Rubles')
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f"{self.name}-{self.rating}%"

# python3 manage.py shell_plus --print-sql
# from movie_app.models import Movie
