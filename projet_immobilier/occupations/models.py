from django.db import models

from app_annonces.models import Annonce
from django.contrib.auth.models import User

# Create your models here.
class Occupation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_occupations' )
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_occupations')
    occupation_type = models.CharField(max_length=20)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='occupations')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.username} - {self.occupation_type}"