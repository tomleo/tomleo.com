# 3rd Party
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView

# App
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def preform_create(self, serializer):
        serializer.save(author=self.request.user)

class HTMLtoReStructuredText(APIView):

    http_method_names = [u'post']
    
    def post(self, request, format=None):
        serializer = ReStructuredTextSerializer(data=request.data)
        if serializer.is_valid():
            #TODO: convert data to HTML
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

