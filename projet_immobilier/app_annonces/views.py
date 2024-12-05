from rest_framework.decorators import api_view ,parser_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Annonce
from .serializers import AnnonceCreateSerializer, AnnonceSerializer
from django.contrib.auth.models import User 
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema




@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Create a new Annonce",
    request_body=AnnonceCreateSerializer,  # Specify the serializer for the request body
    responses={201: AnnonceCreateSerializer}  # Define what the response looks like
)
@parser_classes([MultiPartParser, FormParser]) 
def create_annonce(request):
    """
    Create a new Annonce.
    """
    serializer = AnnonceCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_annonce(request, pk):
    """
    Retrieve a single Annonce by ID.
    """
    try:
        annonce = Annonce.objects.get(pk=pk)
    except Annonce.DoesNotExist:
        return Response({'error': 'Annonce not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AnnonceSerializer(annonce)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_annonce(request, pk):
    """
    Delete an Annonce by ID.
    """
    try:
        annonce = Annonce.objects.get(pk=pk)
    except Annonce.DoesNotExist:
        return Response({'error': 'Annonce not found'}, status=status.HTTP_404_NOT_FOUND)
    annonce.delete()
    return Response({'message': 'Annonce deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_all_annonces(request):
    """
    Retrieve all Annonce objects.
    """
    annonces = Annonce.objects.all().filter(is_occupied=False)
    serializer = AnnonceSerializer(annonces, many=True)  # Serialize all objects
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_annonces_by_owner(request,id):
    owner = User.objects.get(id=id)
    annonces = Annonce.objects.all().filter(owner=owner)
    serializer = AnnonceSerializer(annonces, many=True)  # Serialize all objects
    return Response(serializer.data, status=status.HTTP_200_OK)