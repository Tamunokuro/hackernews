from django import views
from django.urls import path
from . import views

app_name = 'topnews'
urlpatterns = [
    path('', views.home, name='home'),
    path('comments/', views.comments, name='comments'),
    path('jobs/', views.jobs, name='jobs'),
    path('detail/<int:pk>/', views.story_detail, name='story_detail'),
    path('search/', views.search, name='search')
]
