from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=254)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
