
from rest_framework import viewsets

from .models import Commentaire
from .serializers import CommentaireSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Commentaire
from .serializers import CommentaireSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class CommentaireListCreateAPIView(APIView):
   # lookup_field = 'id'
    # GET: List all comments, POST: Create a new comment
    def get(self, request, id=None):
        if id:  # Get a specific Favorite by id
            comm = Commentaire.objects.filter(id=id).first()
            if comm is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CommentaireSerializer(comm)
            return Response(serializer.data)
        else:  # Get a list of all Favorites
            commentaires = Commentaire.objects.all()
            serializer = CommentaireSerializer(commentaires, many=True)
            return Response(serializer.data)


    def post(self, request):

        user = get_object_or_404(User, pk=request.data.get('user'))
        print(user)
        data = {
            'annonce': request.data.get('annonce'),  
            'contenu' :request.data.get('contenu'),
            'user' : user.id  }
        print (request.data.get('user'))
        serializer = CommentaireSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Save the Favorite instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # GET: Retrieve, PUT: Update, DELETE: Delete a single comment
    

    def put(self, request, id=None):
        commentaire = get_object_or_404(Commentaire, pk=id)
        serializer = CommentaireSerializer(commentaire, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        commentaire = get_object_or_404(Commentaire, pk=id)
        commentaire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,data="deleted")

