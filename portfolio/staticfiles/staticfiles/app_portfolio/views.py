from encodings import search_function
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect

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
    context = {"form": create_form}
    if request.method == "POST":
        user = CreateUser(request.POST, request.FILES)

        if user.is_valid():
            user.save()

            context.setdefault("msg", "Successfully Added")
            template = 'users/register.html'
            return render(request, template, context)
        return redirect('user.register')

    template = 'users/register.html'
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
