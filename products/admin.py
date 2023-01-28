from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ To show products on the admin page """

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'weight',
        'intensity',
        'rating',
    )

    ordering = ('sku',)
    search_fields = ('name', 'intensity')


class CategoryAdmin(admin.ModelAdmin):
    """ To show categories on the admin page """

    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
