from rest_framework import viewsets
from .serializer import PropiedadSerializer
from .models import Propiedad

# Create your views here.
class PropiedadViewSet(viewsets.ModelViewSet):
    queryset=Propiedad.objects.all()
    serializer_class=PropiedadSerializer