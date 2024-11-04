# serializers.py
from rest_framework import serializers

from app_annonces.serializers import AnnonceSerializer
from app_annonces.models import Annonce
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    annonce = serializers.PrimaryKeyRelatedField(queryset=Annonce.objects.all())  # Expect an ID for creation
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'annonce', 'created_at']

    def create(self, validated_data):

        favorite = Favorite.objects.create(**validated_data)
        return favorite

    def to_representation(self, instance):
        # Call the original representation method
        representation = super().to_representation(instance)
        # Modify the annonce field to use the AnnonceSerializer
        representation['annonce'] = AnnonceSerializer(instance.annonce).data
        return representation
       