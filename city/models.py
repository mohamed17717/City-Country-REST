from django.db import models
from country.models import Country

# Create your models here.
class City(models.Model):
  """Model definition for City."""

  # TODO: Define fields here
  name = models.CharField(max_length=50)
  country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    """Meta definition for City."""

    verbose_name = 'City'
    verbose_name_plural = 'Cities'

  def __str__(self):
    """Unicode representation of City."""
    return self.name

  # def get_absolute_url(self):
  #   """Return absolute url for City."""
  #   return ('')

  # TODO: Define custom methods here
