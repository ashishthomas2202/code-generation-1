from rest_framework import generics
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

# class UserCreate(generics.CreateAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)