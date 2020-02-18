from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from TwitterClone.tweets.models import Tweet
from TwitterClone.tweets.forms import TweetForm
from TwitterClone.twitterusers.models import TwitterUser
from TwitterClone.notifications.models import Notification
import re


def tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = request.user
            content = data['content']
            my_regex = r"@(\w+)"
            new_tweet = Tweet.objects.create(
                author = u,
                content = content
                   
            )
            if "@" in content:
                result = re.findall(my_regex, content)
                print(result)
                for curresult in result:
                    # get twitteruser 
                    curtwitteruser = TwitterUser.objects.get(user=User.objects.get(username = curresult))
                    if(curtwitteruser):
                        Notification.objects.create(
                            tweetfrom = new_tweet,
                            tweetfor = curtwitteruser

                        )
            
            return HttpResponseRedirect(reverse('profile'))
    else:
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
            form = TweetForm()
            return render(request,"tweet.html",{'form':form,'userprofile':username,'following':following, 'followTweets':followTweets,'logged_in_user_tweet_count':logged_in_user_tweet_count})
            
        
def tweet_detail(request, tweetid):
    username = Tweet.objects.get(id=tweetid).author
    following = 0
    tweet = Tweet.objects.get(id=tweetid)
    follow_status = 0
    
    if request.user.is_authenticated:
        logged_in_twitterUser = TwitterUser.objects.get(user=request.user)
        curuser = TwitterUser.objects.get(user=User.objects.get(username=username))
        print(curuser)
        allTwitterUsers = TwitterUser.objects.all()
        userTweets = Tweet.objects.filter(author=User.objects.get(username=username))
        logged_in_user_tweet_count = userTweets.count
        if curuser.following:
            following = curuser.following.count
        if curuser in logged_in_twitterUser.following.all():
            follow_status = 1
        if curuser == logged_in_twitterUser:
            follow_status = 2

        return render(request,"tweetdetail.html",{'userprofile':username,'following':following, 'followTweets':tweet,'logged_in_user_tweet_count':logged_in_user_tweet_count,'follow_status':follow_status})
   
    
    