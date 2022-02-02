from unicodedata import name
from rest_framework import serializers

from home.models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields= ['id','name','author','pages']