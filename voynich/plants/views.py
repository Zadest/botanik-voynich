from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf import settings
from .models import Plant, Label, Person, Classification

# Create your views here.
def plantOverview(request):
    plants = Plant.objects.all()
    return HttpResponse(f"<html><img src=\"{plants[0].page_image.url}\"</html>")