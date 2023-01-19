from django.test import TestCase


class TestBasketViews(TestCase):
    """
    Test the basket page class
    """
    def test_products_page(self):
        """
        Check the basket page loads
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
