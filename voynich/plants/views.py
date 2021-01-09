from django.shortcuts import render
from .models import Plant, Label, Person, Classification, Publication, PublicationToAuthor

# Create your views here.
def plantOverview(request):
    
    plants = Plant.objects.all()
    pubs = Publication.objects.all()
    authors = Person.objects.all()
    con = PublicationToAuthor.objects.all()
    labels = Label.objects.all()
    classifications = Classification.objects.all()

    context = {"plants" : plants, "pubs" : pubs, "authors" : authors, "pubs" : pubs, "con" : con, "classifications" : classifications, "labels" : labels}
    return render(request,"plants/index.html",context)

def specificPlant(request,id):
    plant = Plant.objects.get(pk=id)
    classifications = Classification.objects.filter(PlantID=plant.pk)
    context = {"plant" : plant, "class" : classifications}
    return render(request,"plants/plant.html",context)