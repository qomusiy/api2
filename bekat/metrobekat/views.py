from django.shortcuts import render
from rest_framework import generics
from .serializer import MetroBekatSerializer
from .models import MetroBekat
# Create your views here.

def index(r):
    return render(r, template_name='index.html', context={'metro':MetroBekat.objects.all()})

class MetroList(generics.ListAPIView):
    queryset = MetroBekat.objects.all()
    serializer_class = MetroBekatSerializer

class MetroCreate(generics.CreateAPIView):
    queryset = MetroBekat.objects.all()
    serializer_class = MetroBekatSerializer

class MetroDelete(generics.DestroyAPIView):
    queryset = MetroBekat.objects.all()
    serializer_class = MetroBekatSerializer
    lookup_field = 'pk'

class MetroUpdate(generics.UpdateAPIView):
    queryset = MetroBekat.objects.all()
    serializer_class = MetroBekatSerializer
    lookup_field = 'pk'