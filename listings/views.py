from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HelloAPIView(APIView):
    """Test API View that returns a simple hello message."""
    
    permission_classes = []  # Allow anyone to access this endpoint
    
    def get(self, request, format=None):
        """Returns a hello message."""
        return Response({
            "message": "Hello, welcome to ALX Travel App API!",
            "status": "success"
        }, status=status.HTTP_200_OK)
