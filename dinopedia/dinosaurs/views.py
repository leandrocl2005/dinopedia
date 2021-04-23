from rest_framework.views import APIView
from .serializers import DinosaurSerializer
from .models import Dinosaur
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class ListDinosaurs(generics.ListAPIView):

  queryset = Dinosaur.objects.all()
  serializer_class = DinosaurSerializer


class HomeDinosaurs(APIView):
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'index.html'

  def get(self, request):
    queryset = Dinosaur.objects.all()
    return Response({'dinosaurs': queryset})
