from rest_framework import serializers

from app_annonces.models import Annonce
from django.contrib.auth.models import User

from users.models import UserProfile
from .models import Commentaire
class UserProfileserializer(serializers.ModelSerializer) : 
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'role']
# Nested serializer for User
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileserializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','profile']
class CommentaireSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Commentaire
        fields = '__all__'

        
class CommentaireCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)  # Takes the user_id in the request
    annonce_id = serializers.IntegerField(write_only=True)  # Takes the annonce_id in the request

    class Meta:
        model = Commentaire
        fields = ['user_id', 'annonce_id', 'contenu']

    def create(self, validated_data):
        # Get the user and annonce objects using the user_id and annonce_id
        user = User.objects.get(id=validated_data['user_id'])
        annonce = Annonce.objects.get(id=validated_data['annonce_id'])

        # Create a new Commentaire instance with the retrieved user and annonce
        commentaire = Commentaire.objects.create(
            user=user,
            annonce=annonce,
            contenu=validated_data['contenu']
        )

        return commentaire