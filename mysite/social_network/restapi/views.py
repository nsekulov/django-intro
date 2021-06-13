from ..models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer