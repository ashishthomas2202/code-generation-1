from rest_framework import viewsets
from .models import ai
from .serializers import aiSerializer
# Create your views here.

class aiViewSet(viewsets.ModelViewSet):
    queryset = ai.objects.all().order_by('name')
    serializer_class = aiSerializer