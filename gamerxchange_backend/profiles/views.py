from django.shortcuts import render
from rest_framework import APIView
from rest_framework import Response
from .models import Profile
from .serializers import ProfileSerializers

# Create your views here.
class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializers(profiles, many=True)
        return Response(serializer.data)