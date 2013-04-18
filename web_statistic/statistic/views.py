from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.contrib import auth
from django.contrib.auth.models import User
from models import *
from datetime import date
from custom_decorators import responding_static_function

def all_users_genrator(params):
    for user in User.objects.all():
        yield user

@responding_static_function('index.html')
def show_page(request):
    profiles = UserProfile.objects.all()\
                                  .order_by('-id')[:6]
    return dict(user=request.user, profiles=profiles)

@responding_static_function('login.html')
def show_login_page(request):
    return 

@responding_static_function('signup.html')
def show_signup_page(request):
    return 

@responding_static_function('blog.html')
def show_blog_page(request):
    return dict(user=request.user)

@responding_static_function('profile.html')
def show_profile_page(request, user_id):
    profile = UserProfile.objects.get(user = User.objects.get(id=user_id))
    return dict(user=request.user, profile=profile)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            user = auth.authenticate(username=str(request.POST['username']), password=str(request.POST['password']))
            if user is not None:
                auth.login(request, user)
                url = "/profile/%s/" %user.id
            else:
                url = "/login/"
        else:
            url = "/login/"
    else:
        return HttpResponse(status=400)
    return HttpResponseRedirect(url)

@csrf_exempt
def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def user_registration(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST and\
         'email' in request.POST:
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'],
                                     email=request.POST['email'])
            new_user = User.objects.create_user(username=request.POST['username'], 
                                                password=request.POST['password'],
                                                email=request.POST['email'])
            new_user.save()
            new_profile = UserProfile(user=new_user, 
                                      date_of_birthday=date.today(), 
                                      profile_picture_url='http://localhost:8000/static/img/765-default-avatar.png')
            new_profile.save()
            next_url = '/login/'
    else:
        next_url = '/signup/'
    return HttpResponseRedirect(next_url)

@csrf_exempt
def responding_current_svg_status(request):
    pass