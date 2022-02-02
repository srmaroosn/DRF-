from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializers
from home import serializers
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets

# Create your views here.
#function based view
@api_view(['GET','POST'])
def blist(request):
    if request.method=='GET':
        book = Book.objects.all()
        serializer = BookSerializers(book,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer= BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def blist_details(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=BookSerializers(book)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer= BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        book.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
#class based view 
class BookAPIview(APIView):
    def get_queryset(self, request):
        book =Book.objects.all()
        return book

    def get(self,request):
        book=self.get_queryset(request)
        serializer =BookSerializers(book, many=True)
        return Response ( serializer.data , status=status.HTTP_204_NO_CONTENT)
    def post(self, request):
        serializer= BookSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response ( serializer.data , status=status.HTTP_204_NO_CONTENT)

class BookAPIviewdetails(APIView):
    def get_object(self, id ):

        try:
            return Book.objects.get(id=id)
       
        except Book.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        book=self.get_object(id)
        serializer =BookSerializers(book)
        return Response ( serializer.data , status=status.HTTP_200_OK)

    def put(self,request,id):
        book= self.get_object(id)
        serializer=BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        book=self.get_object(id)
        book.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#mixing
class Booklistmixin(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class= BookSerializers
    def get(self, request, *args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args,**kwargs):
        return self.create(request,*args,**kwargs)

class BookDetailMixin(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializers
    def get(self, request, *args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self, request, *args,**kwargs):
        return self.update(request,*args,**kwargs)   
    def delete(self, request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class BooklistCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDetail(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

#kjfdlg 
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers






