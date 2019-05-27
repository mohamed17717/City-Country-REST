from rest_framework import serializers
from country.models import Country
from city.models import City


class CountriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = ('name',)

class CitySerializer(serializers.ModelSerializer):
  # country = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = City
    fields = ('name',)

class CityWhereSerializer(serializers.ModelSerializer):
  country = serializers.StringRelatedField(read_only=True)
  class Meta:
    model = City
    fields = ('name', 'country')