from django.db import models


class Contact(models.Model):
    """Подписка на email"""

    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email