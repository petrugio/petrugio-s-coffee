from django.db import models


class Category(models.Model):
    """
    Model for categories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for products
    """
    Mild = 'Mild'
    Medium = 'Medium'
    Strong = 'Strong'
    Intense = 'Intense'

    INTENSITY_CHOICES = [
        (Mild, 'Mild'),
        (Medium, 'Medium'),
        (Strong, 'Strong'),
        (Intense, 'Intense')
    ]

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    weight = models.CharField(max_length=12, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    intensity = models.CharField(choices=INTENSITY_CHOICES,
                                 max_length=24,
                                 default='')
    rating = models.DecimalField(max_digits=6, decimal_places=1,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
