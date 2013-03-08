from django.shortcuts import render_to_response

def show_page(request):
    return render_to_response('index.html')

def show_login_page(request):
    return render_to_response('login.html')

def show_signup_page(request):
    return render_to_response('signup.html')
