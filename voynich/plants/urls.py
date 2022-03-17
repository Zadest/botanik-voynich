from django.urls import path
import re
from . import views

urlpatterns = [
    path('',views.plantOverview, name="index"),
    path('<int:id>/', views.specificPlant ,name="plant"),
    path('rest/plant/<int:pk>/',views.PlantDetail,name='plant-detail'),
    path('rest/classforpage/<int:plantID>/',views.ClassForPage,name='class-plant'),
    path('rest/plants',views.PlantListCreate.as_view()),
    path('rest/persons',views.PersonListCreate.as_view()),
    path('rest/publications',views.PublicationListCreate.as_view()),
    path('rest/publication/<int:pubID>/',views.PublicationDetail,name="pub-detail"),
    path('rest/classifications',views.ClassificationListCreate.as_view())
]