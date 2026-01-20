from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
