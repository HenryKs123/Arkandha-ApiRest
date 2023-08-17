from django.urls import path,include
from rest_framework import routers
from Propietario import views

router = routers.DefaultRouter()
router.register(r'Propietario',views.PropietarioViewSet)

urlpatterns =[
    path('', include(router.urls))
]