from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserProfile
from .models import Annonce
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
class AnnonceSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Annonce
        fields = '__all__'



class AnnonceCreateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   
    class Meta:
        model = Annonce
        fields = '__all__'
    