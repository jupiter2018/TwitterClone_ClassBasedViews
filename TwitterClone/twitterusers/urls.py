from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.Profile_View.as_view(), name='profile'),
    path('myprofile', views.My_Profile_View.as_view(),name='myprofile'),
    path('profile/<str:authorname>/', views.follower_view, name='followerprofile'),
    path('follow/<str:followname>/', views.Add_Follow.as_view(), name='addFollow'),
    # path('profile/<str:followname>/unfollow/<str:unfollowname>/',views.remove_follow, name='removeFollow'),
    path('unfollow/<str:unfollowname>/', views.Remove_Follow.as_view(), name='removefollow')
]