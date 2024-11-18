from rest_framework import serializers

from app_annonces.serializers import AnnonceSerializer
from app_annonces.models import Annonce
from users.models import UserProfile
from .models import Occupation
from django.contrib.auth.models import User


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


# Occupation Serializer with nested User and Annonce
class OccupationSerializer(serializers.ModelSerializer):
    owner = UserSerializer()  # Nested User serializer for owner
    client = UserSerializer()  # Nested User serializer for client
    annonce = AnnonceSerializer()  # Nested Annonce serializer for annonce

    class Meta:
        model = Occupation
        fields = ['id', 'owner', 'client', 'occupation_type', 'annonce', 'start_date', 'end_date', 'is_active']


class OccupationCreateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    annonce = serializers.PrimaryKeyRelatedField(queryset=Annonce.objects.all())

    class Meta:
        model = Occupation
        fields = '__all__'
    