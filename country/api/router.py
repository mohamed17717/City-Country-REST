from rest_framework import routers
from .viewsets import CountriesViewSet

from django.urls import path

router = routers.DefaultRouter()
router.register('', CountriesViewSet, base_name='')
# router.register('random/(?P<name>[^/.]+)/', CountriesViewSet.random, base_name='random')


customRouter = [
  path(r'api/random/<?P<name>\w+/', CountriesViewSet)
]
