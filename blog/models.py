from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    title = models.SlugField(max_length=250)
    bode = models.TextField()

    def __str__(self):
        return self.title
