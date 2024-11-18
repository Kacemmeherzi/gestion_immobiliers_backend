from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)  # Simple string for role

    def __str__(self):
        return f"{self.user.username} - {self.role or 'No role'}"