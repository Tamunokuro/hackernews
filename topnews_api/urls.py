from django.urls import path
from .views import CommentDetail, StoryList, StoryDetail, JobList, CommentList, CreateComment

app_name = 'topnews_api'
urlpatterns = [
    path('', StoryList.as_view(), name='itemlist'),
    path('storydetail/<int:story_id>/', StoryDetail.as_view(),name='storydetail'),
    path('jobs/', JobList.as_view(), name='joblist'),
    path('comments/', CommentList.as_view(), name='commentlist'),
    path('commentdetail/<int:id>/', CommentDetail.as_view(), name='commentdetail'),
    path('createcomment/', CreateComment.as_view(), name='createcomment')
]
