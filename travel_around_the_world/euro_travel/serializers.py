from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import EuroTravel
class EuroTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuroTravel
        fields = "__all__"

new_euro_travel = {"country": "Spain", "tour_cost": 1200, "tour_description": "====___________++++++++++___________"}
