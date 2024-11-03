from django.db import models
from django.contrib.auth.models import User

from app_annonces.models import Annonce

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'annonce')

    def __str__(self):
        return f"{self.user.username} - {self.annonce.titre}"