from django.contrib import admin
from .models import Plant, Label, Person, Classification, Publication, PublicationToAuthor

# Register your models here.
admin.site.register(Plant)
admin.site.register(Label)
admin.site.register(Person)
admin.site.register(Classification)
admin.site.register(Publication)
admin.site.register(PublicationToAuthor)