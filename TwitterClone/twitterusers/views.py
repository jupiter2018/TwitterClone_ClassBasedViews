from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from TwitterClone.twitterusers.models import TwitterUser
from TwitterClone.tweets.models import Tweet
from TwitterClone.notifications.models import Notification
from TwitterClone.authentication.forms import LoginForm
from itertools import chain
from django.views.generic import View

# def profile_view(request):
#     # if(User.is_authenticated):
#     #     username = User.get_username
#     username = None
#     following = 0
#     followTweets = []
#     peopleToFollow = []
#     tweetsnewlist = []
#     notifications = 0
#     if request.user.is_authenticated:
#         username = request.user.username
#         userdata = TwitterUser.objects.filter(user=request.user)
#         curuser = TwitterUser.objects.get(user=request.user)
#         all_notifications = Notification.objects.filter(tweetfor=curuser)
#         notifications = all_notifications.count
#         allTwitterUsers = TwitterUser.objects.all()
#         userTweets = Tweet.objects.filter(author=request.user)
#         logged_in_user_tweet_count = userTweets.count
#         #presentuser = TwitterUser.objects.get(user=request.user)
#         followTweets.append(Tweet.objects.filter(author=request.user))
#         for user in userdata:
#             if user.following:
#                 following = user.following.count
#             else:
#                 following = 0
#             for follow in user.following.all():
#                 followTweets.append(Tweet.objects.filter(author=follow.user))
#         for curtwitteruser in allTwitterUsers:
#             if curtwitteruser not in user.following.all() and not curtwitteruser.user == request.user:
#                 peopleToFollow.append(curtwitteruser)
#         for tweet in followTweets:
#             for curtweet in tweet:
#                 tweetsnewlist.append(curtweet)
#         tweetsnewlist.sort(key=lambda present_tweet: present_tweet.created)
#         print(followTweets)
#         return render(request,"profile.html",{'userprofile':username,'following':following, 'followTweets':tweetsnewlist,'peopleToFollow':peopleToFollow,'logged_in_user_tweet_count':logged_in_user_tweet_count,'notifications':notifications})
#     else:      
#         form = LoginForm()
#         return HttpResponseRedirect(reverse('login'))

class Profile_View(View):
    def get(self, request, *args, **kwargs):
        username = None
        following = 0
        followTweets = []
        peopleToFollow = []
        tweetsnewlist = []
        notifications = 0
        if request.user.is_authenticated:
            username = request.user.username
            userdata = TwitterUser.objects.filter(user=request.user)
            curuser = TwitterUser.objects.get(user=request.user)
            all_notifications = Notification.objects.filter(tweetfor=curuser)
            notifications = all_notifications.count
            allTwitterUsers = TwitterUser.objects.all()
            userTweets = Tweet.objects.filter(author=request.user)
            logged_in_user_tweet_count = userTweets.count
            followTweets.append(Tweet.objects.filter(author=request.user))
            for user in userdata:
                if user.following:
                    following = user.following.count
                else:
                    following = 0
                for follow in user.following.all():
                    followTweets.append(Tweet.objects.filter(author=follow.user))
            for curtwitteruser in allTwitterUsers:
                if curtwitteruser not in user.following.all() and not curtwitteruser.user == request.user:
                    peopleToFollow.append(curtwitteruser)
            for tweet in followTweets:
                for curtweet in tweet:
                    tweetsnewlist.append(curtweet)
            tweetsnewlist.sort(key=lambda present_tweet: present_tweet.created)
            print(followTweets)
            return render(request, "profile.html", {'userprofile':username,'following':following, 'followTweets':tweetsnewlist,'peopleToFollow':peopleToFollow,'logged_in_user_tweet_count':logged_in_user_tweet_count,'notifications':notifications})
        else:      
            form = LoginForm()
            return HttpResponseRedirect(reverse('login'))


# def my_profile_view(request):
#     # if(User.is_authenticated):
#     #     username = User.get_username
#     username = None
#     following = 0
#     followTweets = []
#     peopleToFollow = []
#     if request.user.is_authenticated:
#         username = request.user.username
#         userdata = TwitterUser.objects.filter(user=request.user)
#         allTwitterUsers = TwitterUser.objects.all()
#         userTweets = Tweet.objects.filter(author=request.user)
#         logged_in_user_tweet_count = userTweets.count
#         #presentuser = TwitterUser.objects.get(user=request.user)
#         followTweets.append(Tweet.objects.filter(author=request.user))
#         for user in userdata:
#             if user.following:
#                 following = user.following.count
#             else:
#                 following = 0
            

#         print(followTweets)
#         return render(request,"myprofile.html",{'userprofile':username,'following':following, 'followTweets':followTweets,'logged_in_user_tweet_count':logged_in_user_tweet_count})
#     else:
        
#         form = LoginForm()
#         return HttpResponseRedirect(reverse('login'))

class My_Profile_View(View):
    def get(self, request, *args, **kwargs):
        username = None
        following = 0
        followTweets = []
        peopleToFollow = []
        if request.user.is_authenticated:
            username = request.user.username
            userdata = TwitterUser.objects.filter(user=request.user)
            allTwitterUsers = TwitterUser.objects.all()
            userTweets = Tweet.objects.filter(author=request.user)
            logged_in_user_tweet_count = userTweets.count
            #presentuser = TwitterUser.objects.get(user=request.user)
            followTweets.append(Tweet.objects.filter(author=request.user))
            for user in userdata:
                if user.following:
                    following = user.following.count
                else:
                    following = 0
            print(followTweets)
            return render(request, "myprofile.html", {'userprofile':username,'following':following, 'followTweets':followTweets,'logged_in_user_tweet_count':logged_in_user_tweet_count})
        else:
            
            form = LoginForm()
            return HttpResponseRedirect(reverse('login'))


def follower_view(request,authorname):
    # if(User.is_authenticated):
    #     username = User.get_username
    username = authorname
    following = 0
    followTweets = []
    peopleToFollow = []
    follow_status = 0
    if request.user.is_authenticated:
        logged_in_twitterUser = TwitterUser.objects.get(user=request.user)
        curuser = TwitterUser.objects.get(user=User.objects.get(username=authorname))
        print(curuser)
        allTwitterUsers = TwitterUser.objects.all()
        userTweets = Tweet.objects.filter(author=User.objects.get(username=authorname))
        logged_in_user_tweet_count = userTweets.count
        followTweets.append(Tweet.objects.filter(author=User.objects.get(username=authorname)))
        if curuser.following:
            following = curuser.following.count
        if curuser in logged_in_twitterUser.following.all():
            follow_status = 1
        if curuser == logged_in_twitterUser:
            follow_status = 2

        return render(request,"followerprofile.html",{'userprofile':username,'following':following, 'followTweets':followTweets,'logged_in_user_tweet_count':logged_in_user_tweet_count,'follow_status':follow_status})
    else:
        
        form = LoginForm()
        return HttpResponseRedirect(reverse('login'))

# def add_follow(request, followname):
#     logged_in_twitterUser = TwitterUser.objects.get(user=request.user)
#     newfollow = User.objects.get(username=followname)
#     newfollowTwitteruser = TwitterUser.objects.get(user=newfollow)
#     # combined_followers = logged_in_twitterUser.following.all().union(newfollowTwitteruser)
#     # TwitterUser.objects.filter(user=request.user).update(following=combined_followers)
#     logged_in_twitterUser.following.add(newfollowTwitteruser)
#     return HttpResponseRedirect(reverse('profile'))

class Add_Follow(View):
    def get(self, request, *args, **kwargs):
        logged_in_twitterUser = TwitterUser.objects.get(user=request.user)
        print(args)
        print(kwargs)
        followname = kwargs['followname']
        newfollow = User.objects.get(username=followname)
        newfollowTwitteruser = TwitterUser.objects.get(user=newfollow)
        logged_in_twitterUser.following.add(newfollowTwitteruser)
        return HttpResponseRedirect(reverse('profile'))

# def remove_follow(request, unfollowname):
#     logged_in_twitterUser = TwitterUser.objects.get(user=request.user)
#     newfollow = User.objects.get(username=unfollowname)
#     newfollowTwitteruser = TwitterUser.objects.get(user=newfollow)
#     # combined_followers = logged_in_twitterUser.following.all().union(newfollowTwitteruser)
#     # TwitterUser.objects.filter(user=request.user).update(following=combined_followers)
#     logged_in_twitterUser.following.remove(newfollowTwitteruser)
#     return HttpResponseRedirect(reverse('profile'))

class Remove_Follow(View):
    def get(self, request, *args, **kwargs):
        logged_in_twitterUser = TwitterUser.objects.get(user=request.user)
        newfollow = User.objects.get(username=kwargs['unfollowname'])
        newfollowTwitteruser = TwitterUser.objects.get(user=newfollow)
        # combined_followers = logged_in_twitterUser.following.all().union(newfollowTwitteruser)
        # TwitterUser.objects.filter(user=request.user).update(following=combined_followers)
        logged_in_twitterUser.following.remove(newfollowTwitteruser)
        return HttpResponseRedirect(reverse('profile'))
