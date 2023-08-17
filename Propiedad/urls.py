from django.urls import path,include
from rest_framework import routers
from Propiedad import views

router = routers.DefaultRouter()
router.register(r'Propiedad',views.PropiedadViewSet)

urlpatterns =[
    path('', include(router.urls))
]