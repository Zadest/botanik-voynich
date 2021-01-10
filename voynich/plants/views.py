from django.shortcuts import render
from .models import Plant, Label, Person, Classification, Publication, PublicationToAuthor
import random
# Create your views here.
def plantOverview(request):
    
    plants = Plant.objects.all()
    positions = []
    for i in range(len(plants)):
        positions.append(((str(i*10)+"%",str(random.randint(0,i)*10)+"%")))

    context = {"plants" : plants, "pos" : positions}
    return render(request,"plants/index.html",context)

def specificPlant(request,id):
    plant = Plant.objects.get(pk=id)
    classifications = Classification.objects.filter(PlantID=plant.pk)
    context = {"plant" : plant, "class" : classifications}
    return render(request,"plants/plant.html",context)