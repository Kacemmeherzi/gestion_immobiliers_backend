from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Commentaire
from .serializers import CommentaireCreateSerializer, CommentaireSerializer

# View to list all comments for a particular annonce
@api_view(['GET'])
def get_comments(request, annonce_id):
   
    try:
        commentaires = Commentaire.objects.filter(annonce_id=annonce_id)
        serializer = CommentaireSerializer(commentaires, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Commentaire.DoesNotExist:
        return Response({'error': 'Commentaires not found for this annonce.'}, status=status.HTTP_404_NOT_FOUND)

# View to create a new comment
@api_view(['POST'])
def create_comment(request):
    serializer = CommentaireCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the comment with the user and annonce
     #    comm = CommentaireSerializer(serializer).data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

# View to delete a specific comment by id
@api_view(['POST'])
def delete_comment(request, comment_id):
   
    try:
        comment = Commentaire.objects.get(id=comment_id)
        comment.delete()
        return Response({'message': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Commentaire.DoesNotExist:
        return Response({'error': 'Comment not found.'}, status=status.HTTP_404_NOT_FOUND)
