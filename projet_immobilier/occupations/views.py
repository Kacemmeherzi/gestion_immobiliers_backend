
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OccupationSerializer
from .models import Occupation
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response

@api_view(['POST'])
def create_occupation(request):
    if request.method == 'POST':
        serializer = OccupationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Saves the Occupation to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_occupations_by_owner(request, user_id):
   
    try:
        user = get_object_or_404(User, pk=user_id)
        occupations_as_owner = Occupation.objects.filter(owner=user)

        

        # Serialize the occupations
        serializer = OccupationSerializer(occupations_as_owner, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_occupations_by_client(request, user_id):
   
    try:
        user = get_object_or_404(User, pk=user_id)
        occupations_as_client = Occupation.objects.filter(client=user)

        # Serialize the occupations
        serializer = OccupationSerializer(occupations_as_client, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all_occupations(request):
    """
    Retrieve all occupations from the database.
    """
    try:
        occupations = Occupation.objects.all()  # Fetch all occupations
        # Serialize the occupations
        serializer = OccupationSerializer(occupations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)