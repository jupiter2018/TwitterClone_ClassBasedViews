from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from TwitterClone.authentication.forms import LoginForm
from TwitterClone.twitterusers.models import TwitterUser
from django.views.generic.edit import FormView


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            username = form.cleaned_data.get('username')
            u = User.objects.get(username=data['username'])
            TwitterUser.objects.create(
                user = u,
                
            )
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, "register.html",{'form':form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             #form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username,password=password)
#             #messages.error(request, f'Dont have an account, please sign up')
#             if user:
#                 login(request,user)
#                 return HttpResponseRedirect(request.GET.get("next", "/profile"))
#     else:
#         form = LoginForm()
#         return render(request, "login.html",{'form':form})
#     # return HttpResponseRedirect(reverse('login'))


class Login_View(FormView):
    form_class = LoginForm
    success_url = '/profile'
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
        return super(Login_View, self).form_valid(form)
        