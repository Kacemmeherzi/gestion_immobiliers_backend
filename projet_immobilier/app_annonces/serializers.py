from rest_framework import serializers
from django.contrib.auth.models import User

from occupations.models import Occupation
from .models import Annonce

class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = '__all__'



class AnnonceCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   
    class Meta:
        model = Occupation
        fields = '__all__'
    