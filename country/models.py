from django.db import models

# Create your models here.
class Country(models.Model):
  """Model definition for Country."""

  # TODO: Define fields here
  name = models.CharField(max_length=50)

  class Meta:
    """Meta definition for Country."""

    verbose_name = 'Country'
    verbose_name_plural = 'Countries'

  def __str__(self):
    return self.name

  # def get_absolute_url(self):
  #   """Return absolute url for Country."""
  #   return ('')

  # TODO: Define custom methods here
