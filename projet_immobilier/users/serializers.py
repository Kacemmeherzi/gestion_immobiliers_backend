from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True, min_length=6)
    phone_number = serializers.CharField(max_length=15)
    role = serializers.CharField(max_length=50)

    def create(self, validated_data):
        # Create the user using the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        
        # Now create the user profile
        UserProfile.objects.create(
            user=user,
            phone_number=validated_data['phone_number'],
            role=validated_data['role']
        )
        
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError('Both username and password are required.')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials. Please try again.')

        if not user.is_active:
            raise serializers.ValidationError('User account is deactivated.')

        # Attach the authenticated user to the serializer
        attrs['user'] = user
        return attrs
