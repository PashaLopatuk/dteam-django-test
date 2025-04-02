from api.cv.serializers import CVSerializer
from main.models import CV
from rest_framework import generics


class CVListCreateView(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
