from django.db import models

from catalogue.models.shows import Shows


class Prices(models.Model):
    type = models.CharField(max_length=30, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    shows = models.ManyToManyField(Shows, related_name='shows')

    def __str__(self):
        return f"{self.type} - {self.price}"