"""TwitterClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TwitterClone.authentication.urls import urlpatterns as authentication_urls
from TwitterClone.twitterusers.urls import urlpatterns as twitterusers_urls
from TwitterClone.tweets.urls import urlpatterns as tweets_urls
from TwitterClone.notifications.urls import urlpatterns as notifications_urls
from TwitterClone.twitterusers.models import TwitterUser
from TwitterClone.tweets.models import Tweet
from TwitterClone.notifications.models import Notification
admin.site.register(TwitterUser)
admin.site.register(Tweet)
admin.site.register(Notification)

urlpatterns = [
    path('admin/', admin.site.urls),
    

]
urlpatterns += authentication_urls
urlpatterns += twitterusers_urls
urlpatterns += tweets_urls
urlpatterns += notifications_urls
