from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=50)
    publication = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    cover_image = models.ImageField(default=None)

    def __str__(self):
        return self.name
