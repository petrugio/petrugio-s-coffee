from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Test the home page class
    """
    def test_home_page(self):
        """
        Check the home page loads
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
