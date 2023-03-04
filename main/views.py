from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Tweet
from .serializers import UserSerializer, TweetSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()

class UserView(APIView):
    
    serializer_class = UserSerializer
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.username)})        

class TweetView(APIView):
        
        serializer_class = TweetSerializer
        
        def get(self, request):
            tweets = Tweet.objects.all()
            serializer = TweetSerializer(tweets, many=True)
            return Response({"tweets": serializer.data})
    
        def post(self, request):
            tweet = request.data.get('tweet')
            serializer = TweetSerializer(data=tweet)
            if serializer.is_valid(raise_exception=True):
                tweet_saved = serializer.save()
            return Response({"success": "Tweet '{}' created successfully".format(tweet_saved.content)})


def home(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('/home')
    return render(request, "home.html", {"user": user})
