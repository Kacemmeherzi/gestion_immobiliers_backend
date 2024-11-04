from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from app_annonces.models import Annonce



class Commentaire(models.Model):
    annonce = models.ForeignKey(Annonce, related_name="commentaires", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.user.username} sur {self.annonce.titre}"
