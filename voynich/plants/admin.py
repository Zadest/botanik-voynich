from django.contrib import admin
from .models import Plant, Label, Person, Classification 

# Register your models here.
admin.site.register(Plant)
admin.site.register(Label)
admin.site.register(Person)
admin.site.register(Classification)