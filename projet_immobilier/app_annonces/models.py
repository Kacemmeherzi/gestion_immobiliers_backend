from django.db import models

class Annonce(models.Model):
    CATEGORY_CHOICES = [
        ('vente', 'Vente'),
        ('location', 'Location'),
    ]

    titre = models.CharField(max_length=200)
    localisation = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    nombre_de_chambres = models.IntegerField()
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    image  =  models.CharField(max_length=300,default="no image added")
    equiped = models.BooleanField(default=False)
    lease_duration = models.IntegerField(null=True, blank=True)  # Relevant for renting
    is_negotiable = models.BooleanField(default=False)  # Relevant for selling


    def __str__(self):
        return self.titre
