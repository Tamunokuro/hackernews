from cgitb import lookup
from multiprocessing import context
from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework import generics, filters
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render, reverse, get_object_or_404

from topnews.models import Story, Comment, Job
from .serializers import StorySerializer, JobSerializer, CommentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
# Create your views here.

class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class StoryList(generics.ListCreateAPIView):
    queryset = Story.objects.all().order_by("-created")
    permission_classes = [AllowAny]
    serializer_class = StorySerializer
    filter_backends = [filters.SearchFilter]
    search_filters = ['=item_type','=story_id', '=slug']

class StoryDetail(generics.ListAPIView):
    queryset = Comment.objects.select_related('story_id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    print(queryset)
    
    
    

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by("-created")
    permission_classes = [AllowAny]
    serializer_class = JobSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all().order_by("-created")
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer

class CreateComment(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer




class CommentDetail(MultipleFieldLookupMixin, generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.select_related('story_id').order_by("-created")
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    lookup_fields = ['id']



   

