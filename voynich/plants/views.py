from django.shortcuts import render
from .models import Plant, Label, Person, Classification, Publication, PublicationToAuthor
import random
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

