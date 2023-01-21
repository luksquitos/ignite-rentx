import rest_framework
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.api.viewsets import CarroViewset

router = DefaultRouter()
router.register('cars', CarroViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]


