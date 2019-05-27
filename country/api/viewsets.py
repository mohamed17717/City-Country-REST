from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from country.models import Country
from city.models import City
from .serializers import (
  CountriesSerializer, 
  CitySerializer,
  CityWhereSerializer
)

from random import shuffle

from django.shortcuts import get_list_or_404

# class CountriesViewSet(viewsets.ModelViewSet):
#   queryset = Country.objects.all()
#   serializer_class = CountriesSerializer

class CountriesViewSet(viewsets.ViewSet):

  # /api/
  def list(self, request):
    """ Return all countries """
    countries = Country.objects.all()
    serializer = CountriesSerializer(countries, many=True)
    return Response(serializer.data)

  # /api/{{ countryId }}/
  def retrieve(self, request, pk=None, slug=None):
    """ return all cities in this country depend on id """
    cities = get_list_or_404(City, country=pk)
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

  # /api/{{ countryName }}/cities 
  @action(methods=['get'], detail=True)
  def cities(self, request , pk):
    """ return all cities in this country depend on country name """
    pk = pk.title().replace('-', ' ')

    country = get_list_or_404(Country, name=pk)
    country = country.pop()

    cities  = get_list_or_404(City, country=country.id)
    serializer = CitySerializer(cities, many=True)

    return Response(serializer.data)

  # /api/{{ cityName }}/where/
  @action(methods=['get'], detail=True)
  def where(self, request, pk):
    """ return city in which country """
    pk = pk.title().replace('-', ' ')

    cities = get_list_or_404(City , name=pk)
    serializer = CityWhereSerializer(cities, many=True)

    return Response(serializer.data)


  # @action(methods=['get'], detail=False, url_path=r'random/(?P<name>[^/.]+)', url_name='random')
  # def random(self, request, name):
  #   return Response(name)

  def chooseRandomElms(self, arr, number=1):
    shuffle(arr)
    shuffle(arr)
    return arr[:number]

  @action(methods=['get'],detail=False,url_path=r'random/(?P<number>[\d]+)/countries',url_name='random-countries')
  def randomCountries(self, request, number):
    number = int(number)

    countries = Country.objects.all()
    serializer = CountriesSerializer(countries, many=True)

    return Response(  self.chooseRandomElms( serializer.data, number ) )
  


  @action(methods=['get'], detail=False, url_path=r'random/(?P<number>[\d]+)/cities/(?P<country>[\w]+)', url_name='random-cities')
  def randomCities(self, request, number, country):
    number = int(number)

    # country might be int(countrId) or string(countryName)
    try:
      country = int(country)
      cities = get_list_or_404(City, country= country)
    except:
      country = country.title().replace('-', ' ')
      country = get_list_or_404(Country, name=country)
      country = country.pop()
      cities  = get_list_or_404(City, country= country.id)

    serializer = CountriesSerializer(cities, many=True)

    return Response( self.chooseRandomElms( serializer.data, number ) )
