from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1500)
    director = models.ForeignKey(Director, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='movies', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=250)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    # esli est tovar pomogaet obratitsya k otzyvu i naobarot
    def __str__(self):
        return self.text

# Вывести на страницу один фильм (Movie), его отзывы (Review) и режисcера (Director) данного фильма -  127.0.0.1:8000/movies/<int:id>/