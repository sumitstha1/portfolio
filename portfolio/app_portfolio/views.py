from email import message
from encodings import search_function
from multiprocessing import context
from re import template
from socket import timeout
from django.shortcuts import render, redirect
from django.contrib import messages

from app_portfolio.forms import UserLogin, CreateUser
from .models import AppUser

# Create your views here.
def login_page(request):
    template = 'users/login.html'
    user_form = UserLogin()
    context = {'form': user_form}
    if request.method == 'POST':
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')
        user = AppUser.objects.get(email=req_email)
        if req_email == user.email and req_password == user.password:
            request.session["session_email"] = user.email
            return redirect('starting')
        return render(request, template, context)
    return render(request, template, context)


def register_page(request):
    create_form = CreateUser()
    context = {
        'form': create_form
    }
    template = 'users/register.html'
    if request.method == "POST":
        user = CreateUser(request.POST, request.FILES)

        if user.is_valid():
            user.save()
            return redirect('user.login')
        else:
            return render(request, template, context)
    messages.add_message(request, messages.SUCCESS, f"Thanks for making an appointment, we will email you ASAP!")
    messages.add_message(request, messages.ERROR, f"Something Went wrong")  
    return render(request, template, context)


def start_page(request):
    if not request.session.has_key('session_email'):
        return redirect("user.login")
    template = 'portfolio/starting.html'
    return render(request, template)

def contact_page(request):
    if not request.session.has_key('session_email'):
        return redirect("user.login")
    template = 'portfolio/contact.html'
    return render(request, template)

def project_page(request):
    if not request.session.has_key('session_email'):
        return redirect("user.login")

    template = 'portfolio/projects.html'
    return render(request, template)

def port_index(request):
    if not request.session.has_key('session_email'):
        return redirect("user.login")
    template = 'portfolio/index.html'
    return render(request, template)
