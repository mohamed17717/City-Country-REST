# to run throw manage.py shell
# ./manage.py shell < writeJsonToDb.py

# note i discard any countre with more than 100 city

from country.models import Country
from city.models import City

import json


fileName = 'countries.json'
with open(fileName) as f: 
  countries = json.loads(f.read())

totalCountries = len(countries)
countryNumber = 0

print('Note: i add to db only countries with less than 100 city to be faster, it just for testing purposes')

for country, cities in countries.items():
  countryNumber += 1
  print(countryNumber, country, str(round(countryNumber/totalCountries, 2) * 100)+'%')
  if len(cities) > 100: continue

  country = Country(name=country)
  country.save()

  for city in cities:
    city = City(name= city, country=country)
    city.save()


print('Done!!')
