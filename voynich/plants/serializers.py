from rest_framework import serializers
from .models import Plant, Label, Person, Publication, Classification



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','first_name','last_name')

class PublicationSerializer(serializers.ListSerializer):
    class Meta:
        model = Publication
        fields = ('id','name','year')


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    classifications = ClassificationSerializer(many=True)
    class Meta:
        model = Plant
        fields = ['id','page','page_image','svg','classifications']
