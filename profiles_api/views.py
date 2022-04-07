from email import message
from pickle import NONE
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
# Create your views here.


class HelloWorldApi(APIView):
    """testing api"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({"message":"HelloWorld", "Api_view":an_apiview})

    def post(self, request):
        """Adding an api"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = "hello "+str(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handles updating objects"""
        return Response({"method":"PUT"})

    def patch(self, request, pk=None):
        """handles a partial update on objects"""
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        """handles a deletion on objects"""
        return Response({"method":"DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Rteurn a hello message"""

        a_viewset = ['Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',]

        return Response({"message":"Hello user", "viewset":a_viewset})

    def create(self, request):
        """creates a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hello {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieves a message by its id"""
        return Response({"http_method":"GET"})

    def update(self, request, pk=None):
        """updates a message by its id"""
        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        """partially updates a message by its id"""
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        """removing a message by its id"""
        return Response({"http_method":"DELETE"})
