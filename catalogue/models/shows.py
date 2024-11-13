from django.db import models


class Shows(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()


    def __str__(self):
        return self.name
