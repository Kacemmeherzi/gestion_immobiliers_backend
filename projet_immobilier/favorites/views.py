from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Favorite
from .serializers import CreateFavoriteSerializer, FavoriteSerializer
# pk used maa generics default given class or lookup_field = 'id' if nestaaml class and apiview

@api_view(['GET'])
def get_favorites_by_user(request, id):
    
    try:
        favorites = Favorite.objects.filter(user_id=id)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Favorite.DoesNotExist:
        return Response({"error": "Favorites not found for the given user."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_favorite(request):
    
    serializer = CreateFavoriteSerializer(data=request.data)
    if serializer.is_valid():
        favorite = serializer.save()

        return Response({"message": "Favorite created successfully.","favorite": FavoriteSerializer(favorite).data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    
@api_view(['POST'])
def delete_favorite(request, id):
    favorite = Favorite.objects.filter(id=id).first()
    if favorite is None:
        return Response({"error": "Favorite not found."}, status=status.HTTP_404_NOT_FOUND)
    
    favorite.delete()
    return Response({"message": "Favorite deleted successfully."}, status=status.HTTP_200_OK)
