from rest_framework.serializers import ModelSerializer
from .models import Dinosaur


class DinosaurSerializer(ModelSerializer):
  class Meta:
    model = Dinosaur
    fields = ('id', 'name', 'description', 'photo')