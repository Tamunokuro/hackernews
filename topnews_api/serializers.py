from dataclasses import field
from rest_framework import serializers
from topnews.models import Job, Comment, Story

class JobSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Job
        fields = "__all__"
        read_only_fields = ('created',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = "__all__"
        read_only_fields = ('created','updated',)


class StorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Story
        fields = "__all__"
        read_only_fields = ('created','updated',)

