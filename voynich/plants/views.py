from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Plant, Label, Person, Classification

# Create your views here.
def plantOverview(request):
    plants = Plant.objects.all()
    #template = loader.get_template('plants/index.html')
    context = {
        "plants" :  plants
    }
    return HttpResponse("<img src="+plants[0].page_image.url+">")