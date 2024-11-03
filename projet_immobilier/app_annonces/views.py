from rest_framework import generics
from .models import Annonce
from .serializers import AnnonceSerializer

class AnnonceListCreate(generics.ListCreateAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer

class AnnonceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
