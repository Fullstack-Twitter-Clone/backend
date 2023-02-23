from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Tweet
from .serializers import UserSerializer, TweetSerializer

def home(response, id):
    user = User.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % user.username)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
