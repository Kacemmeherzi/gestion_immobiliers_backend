# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Favorite
from .serializers import FavoriteSerializer
from django.contrib.auth.models import User
# Create a favorite
class AddFavoriteView(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
   # permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# List all favorites
class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
   # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']  # Get the user_id from the URL parameters
        try:
            user = User.objects.get(id=id)  # Check if the user exists
        except User.DoesNotExist:
            return Favorite.objects.none()  # Return an empty queryset if the user does not exist
        
        # Return favorites for the specified user
        return Favorite.objects.filter(user=user)



# Retrieve a specific favorite
class FavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
   # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']  # Get the user_id from the URL parameters
        try:
            favorite = Favorite.objects.get(id=id) 
        except Favorite.DoesNotExist:
            return Favorite.objects.none()  # Return an empty queryset if the user does not exist
        
        
        # Return favorites for the specified user
        return   favorite 
