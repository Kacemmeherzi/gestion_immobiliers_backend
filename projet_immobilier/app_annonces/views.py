from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Annonce
from .serializers import AnnonceSerializer

@api_view(['POST'])
def create_annonce(request):
    """
    Create a new Annonce.
    """
    serializer = AnnonceSerializer(data=request.data)
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
    annonces = Annonce.objects.all()
    serializer = AnnonceSerializer(annonces, many=True)  # Serialize all objects
    return Response(serializer.data, status=status.HTTP_200_OK)