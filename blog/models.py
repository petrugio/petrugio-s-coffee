from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Blog(models.Model):
    """Blog model"""

    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """Sorts blog posts in descending order"""
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
