from django.db import models
class EuroTravel(models.Model):
    country = models.CharField(max_length=100)
    tour_cost = models.IntegerField()
    tour_description = models.TextField()
    def __str__(self):
        return f"{self.pk} - {self.country} - {self.tour_cost} - {self.tour_description}"


