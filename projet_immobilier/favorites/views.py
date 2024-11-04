from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app_annonces.models import Annonce
from .models import Favorite
from .serializers import FavoriteSerializer
from django.contrib.auth.models import User
# pk used maa generics default given class or lookup_field = 'id'
class FavoriteView(APIView):
    
    def get(self, request, id=None):
        if id:  # Get a specific Favorite by id
            favorite = Favorite.objects.filter(id=id).first()
            if favorite is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data)
        else:  # Get a list of all Favorites
            favorites = Favorite.objects.all()
            serializer = FavoriteSerializer(favorites, many=True)
            return Response(serializer.data)


    def post(self, request):
        data = {
            'annonce': request.data.get('annonce'),  # Expect annonce ID
            'user': request.data.get('user')  # Expect user ID from the request body
        }
        # Create the serializer instance with the prepared data
        serializer = FavoriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Save the Favorite instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    

    def delete(self, request, id):
        # Delete a Favorite by id
        favorite = Favorite.objects.filter(id=id).first()
        if favorite is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,data="deleted")
