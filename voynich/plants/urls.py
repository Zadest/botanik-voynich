from django.urls import path

from . import views

urlpatterns = [
    path('',views.plantOverview, name="index"),
    path('<int:id>/', views.specificPlant ,name="plant")
]