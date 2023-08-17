from rest_framework import viewsets
from .serializer import PropietarioSerializer
from .models import Propietario

# Create your views here.
class PropietarioViewSet(viewsets.ModelViewSet):
    queryset=Propietario.objects.all()
    serializer_class=PropietarioSerializer