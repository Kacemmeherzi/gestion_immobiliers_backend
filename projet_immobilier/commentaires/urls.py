from django.urls import path
from .views import   create_comment, delete_comment, get_comments




urlpatterns = [
    path('getall/<int:annonce_id>', get_comments, name='get_comments'),
    path('create', create_comment, name='create_comment'),
    path('delete/<int:comment_id>', delete_comment, name='delete_comment'),
]

