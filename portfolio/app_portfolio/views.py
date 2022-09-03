from encodings import search_function
from re import template
from django.shortcuts import render

# Create your views here.
def start_page(request):
    template = 'portfolio/starting.html'
    return render(request, template)

def contact_page(request):
    template = 'portfolio/contact.html'
    return render(request, template)

def port_index(request):
    template = 'portfolio/index.html'
    return render(request, template)