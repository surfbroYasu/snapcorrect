from django.db import models
from django.contrib.auth.models import User

class Joke(models.Model):
    joke_id = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.content

class JokeComment(models.Model):
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.joke.content[:30]}"

class FavoriteJoke(models.Model):
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.joke.content[:30]}"
