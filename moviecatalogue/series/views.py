from django.shortcuts import render
from rest_framework import generics
from .serializers import SerieSerializer
from .models import Serie
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new serie."""
        serializer.save()

