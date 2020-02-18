from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from TwitterClone.notifications.models import Notification
from TwitterClone.twitterusers.models import TwitterUser

def notification_view(request):
    notifications = 0
    print(notifications)
    all_notifications = []
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        curuser = TwitterUser.objects.get(user=request.user)
        notification_queryset = Notification.objects.filter(tweetfor=curuser)
        notifications = notification_queryset.count()
        if not notifications == 0:
            for notification in notification_queryset:
                all_notifications.append(notification)

        print(all_notifications)
        print(notifications)
        Notification.objects.all().delete()
        return render(request,"notification.html",{'username':username,'all_notifications':all_notifications,'notifications':notifications})
    
    return HttpResponseRedirect(reverse('login'))
