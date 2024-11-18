# serializers.py
from rest_framework import serializers

from app_annonces.serializers import AnnonceSerializer
from app_annonces.models import Annonce
from .models import Favorite
from rest_framework import serializers
from .models import Favorite, User, Annonce

class FavoriteSerializer(serializers.ModelSerializer):
  #  annonce = serializers.PrimaryKeyRelatedField(queryset=Annonce.objects.all())  # Expect an ID for creation
    annonce = AnnonceSerializer()
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'annonce', 'created_at']

    def create(self, validated_data):

        favorite = Favorite.objects.create(**validated_data)
        return favorite

 #   def to_representation(self, instance):
        # Call the original representation method
        representation = super().to_representation(instance)
        # Modify the annonce field to use the AnnonceSerializer
        representation['annonce'] = AnnonceSerializer(instance.annonce).data
        return representation



class CreateFavoriteSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    annonce_id = serializers.IntegerField()

    def validate(self, data):
        """
        Validate that both user and annonce exist and the Favorite is unique.
        """
        user_id = data.get('user_id')
        annonce_id = data.get('annonce_id')

        # Validate User
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")

        # Validate Annonce
        try:
            annonce = Annonce.objects.get(id=annonce_id)
        except Annonce.DoesNotExist:
            raise serializers.ValidationError("Annonce does not exist.")

        # Validate uniqueness
        if Favorite.objects.filter(user=user, annonce=annonce).exists():
            raise serializers.ValidationError("This favorite already exists.")

        return data

    def create(self, validated_data):
        """
        Create a new Favorite instance.
        """
        user = User.objects.get(id=validated_data['user_id'])
        annonce = Annonce.objects.get(id=validated_data['annonce_id'])
        favorite = Favorite.objects.create(user=user, annonce=annonce)
        return favorite
