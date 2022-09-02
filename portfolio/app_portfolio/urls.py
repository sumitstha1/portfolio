from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='starting'),
    path('index/', views.port_index, name='index'),
]