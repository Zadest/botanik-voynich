from django.db.models.query import QuerySet
from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Plant, Label, Person, Classification, Publication, PublicationToAuthor
from .serializers import PlantSerializer, PersonSerializer, PublicationSerializer, ClassificationSerializer
from rest_framework import generics
import random

from plants import serializers

class PlantListCreate(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PublicationListCreate(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer  

class ClassificationListCreate(generics.ListCreateAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer   

@api_view(['GET'])
def PlantDetail(request,pk):
    query = Plant.objects.get(id=pk)
    serializer = PlantSerializer(query,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ClassForPage(request,plantID):
    query = Classification.objects.filter(PlantID=plantID)
    if not query:
        return Response(None)
    serializers = ClassificationSerializer(query,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def PublicationDetail(request,pubID):
    query = Publication.objects.get(id=pubID)
    serializer = PublicationSerializer(query,many=False)
    return Response(serializer.data)

# Create your views here.
def plantOverview(request):
    plants = Plant.objects.all()
    positions = []
    for i in range(len(plants)):
        positions.append("x=\""+str(i*10)+"% y=\""+str(random.randint(0,i)*10)+"%")

    context = {"plants" : plants, "pos" : positions}
    return render(request,"plants/index.html",context)


def specificPlant(request,id):
    plant = Plant.objects.get(pk=id)
    classifications = Classification.objects.filter(PlantID=plant.pk)
    pubs = []
    for classi in classifications:
        pubs += Publication.objects.filter(name=classi.PublicationID)
    context = {"plant" : plant, "class" : classifications, "pubs" : pubs}
    return render(request,"plants/plant.html",context)

