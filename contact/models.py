from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """ Model for contact, allows the user
    to send a message to site owner/admin """

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """
        Meta data for the contact app
        """
        verbose_name_plural = 'Contact'
        ordering = ('-date_sent',)
