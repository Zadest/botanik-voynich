from django.db import models

# Create your models here.
class Plant(models.Model):
    page = models.CharField(max_length=10)
    page_image = models.ImageField(upload_to="site_media")
    svg = models.FileField()
    def __str__(self):
        return self.page

class Label(models.Model):
    plant_Id = models.ForeignKey(Plant, on_delete=models.CASCADE)
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

class Classification(models.Model):
    plant_Id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    person_Id = models.ForeignKey(Person, on_delete=models.CASCADE)
    year = models.DateField(blank=True)
    descr = models.CharField(max_length=255,blank=True)
    source = models.CharField(max_length=255,blank=True)
    real_image = models.ImageField(blank=True)
    medievial_image = models.ImageField(blank=True)


