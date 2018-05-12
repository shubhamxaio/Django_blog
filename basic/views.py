from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

def login_user(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        if user:
            # request.session['user_name'] = user.first_name
            return redirect('home')
        msg = 'Invalid username/password. You can remmber try it again as we don\'t forget password option!'
    return render(request, 'login.html', {'msg': msg})


def signup(request):
    msg = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            return redirect('login_user')
        else:
            msg = 'Form validation fails!!'
            return render(request, 'signup.html', {'form': form, 'msg': msg})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'msg': msg})


def logout_user(request):
    logout(request)
    return redirect('login')


# @login_required()
def home(request):
    # user = request.session['temp_data']
    # print(request.session['temp_data'])
    blogs = Blog().get_active_blogs()
    return render(request, 'home.html', {'blogs': blogs})


def create_post(request):
    msg = None
    error_msg = None
    if request.method == 'POST':
        data = {}
        data['title'] = request.POST['title']
        data['description'] = request.POST['description']
        blog_created = Blog().create_blog(data)
        if blog_created is True:
            msg = 'Your post [ %s ] has been saved successfully in our database' % (data['title'])
        else:
            error_msg = 'Something went wrong!! Contact administrator'
        return render(request, 'create_post.html', {'msg': msg, 'error_msg': error_msg})
    return render(request, 'create_post.html', {'msg': msg, 'error_msg': error_msg})


def delete_post(request, blog_id):
    Blog().delete_blog(blog_id)
    return redirect('home')

def view_blog(request, blog_id, title):
    Blog()
