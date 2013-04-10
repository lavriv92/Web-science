from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.contrib import auth
from django.contrib.auth.models import User

def all_users_genrator(params):
    for user in User.objects.all():
        yield user


def show_page(request):
    return render_to_response('index.html', dict(user=request.user))

def show_login_page(request):
    return render_to_response('login.html')

def show_signup_page(request):
    return render_to_response('signup.html')

def show_blog_page(request):
    return render_to_response('blog.html', dict(user=request.user))

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            user = auth.authenticate(username=str(request.POST['username']), password=str(request.POST['password']))
            if user is not None:
                auth.login(request, user)
            else:
                error = "Authorization failed!!!"
    return HttpResponseRedirect('/')

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
            next_url = '/login/'
    else:
        next_url = '/'
    return HttpResponseRedirect(next_url)
