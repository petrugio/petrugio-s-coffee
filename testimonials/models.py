from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Testimonials(models.Model):
    """Testimonials model"""

    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonial")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name_plural = 'Testimonials'
        """Sorts testimonials in descending order"""
        ordering = ["-created"]

    def __str__(self):
        return self.title
