from django.db import models
# Create your models here.
class Plant(models.Model):
    page = models.CharField(max_length=10)
    page_image = models.ImageField(upload_to="imgs/")
    svg = models.FileField(upload_to="imgs/")
    def __unicode__(self):
        return '"name":%s,"page_image":"%s","svg":"%s"'%(self.page , self.page_image, self.svg)
    def __str__(self):
        return '"name":%s,"page_image":"%s","svg":"%s"'%(self.page , self.page_image, self.svg)

class Label(models.Model):
    PlantID = models.ForeignKey(Plant, on_delete=models.CASCADE)
    Label = models.CharField(max_length=255)

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    misc = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.last_name+", "+self.first_name

class Publication(models.Model):
    name = models.CharField(max_length=255)
    year = models.DateField(blank=True)
    authors = models.ManyToManyField(Person)

    def __str__(self):
        return self.name

class PublicationToAuthor(models.Model):
    PublicationID = models.ForeignKey(Publication, on_delete=models.CASCADE)
    AuthorID = models.ForeignKey(Person, on_delete=models.CASCADE)

class Classification(models.Model):
    PlantID = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='classifications')
    PublicationID = models.ForeignKey(Publication, on_delete=models.CASCADE)
    year = models.DateField(blank=True)
    descr = models.CharField(max_length=255,blank=True)
    source = models.CharField(max_length=255,blank=True)
    real_image = models.ImageField(blank=True, upload_to="imgs/")
    medieval_image = models.ImageField(blank=True, upload_to="imgs/")

    class Meta:
        unique_together = ('PlantID','PublicationID')

    def __unicode__(self):
        return '%s,%s,%s'% (self.id,self.PlantID.id,self.PublicationID.id)
    
    def __str__(self):
        return '%s,%s,%s'% (self.id,self.PlantID.id,self.PublicationID.id)
    


