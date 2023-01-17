from django.test import TestCase


class TestProductsViews(TestCase):
    """
    Test the products page class
    """
    def test_products_page(self):
        """
        Check the products page loads
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
