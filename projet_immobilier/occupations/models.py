from django.db import models

from app_annonces.models import Annonce

# Create your models here.
class Occupation(models.Model):
  #  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='occupations')
  #  client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='occupations')
    occupation_type = models.CharField(max_length=20)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='occupations')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.occupation_type.name}"