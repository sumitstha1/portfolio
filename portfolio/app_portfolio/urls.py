from django.urls import path, include
from . import views
from django.contrib import admin
from hospitalmanager.views import HomeTemplateView

urlpatterns = [
    
    # user login
    path('login/', views.login_page, name='user.login'),
    path('register/', views.register_page, name='user.register'),
    

    # pages
    path('', views.start_page, name='starting'),
    path('index/', views.port_index, name='index'),
    path('contact/', views.contact_page, name='contact'),
    path('projects/', views.project_page, name='project'),
    path('hospital/', HomeTemplateView.as_view(), name = 'hospital'),
]