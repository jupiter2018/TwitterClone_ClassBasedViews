from django.urls import path
from . import views

urlpatterns = [
    path('tweet/', views.tweet_view, name='tweet'),
    path('tweet/<int:tweetid>/', views.tweet_detail, name='tweetdetail')
    # path('tweet/<int:tweetid>/unfollow/<str:unfollowname>/',views.remove_follow, name='removeFollow'),
    
]