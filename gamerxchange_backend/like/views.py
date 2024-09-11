from django.shortcuts import render
from rest_framework import generics, permissions
from like.models import Like
from .serializers import LikeSerializer

# Create your views here.
class LikeList(generics.ListCreateAPIView):
    
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Like.objects.all()
        serializer_class = LikeSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]