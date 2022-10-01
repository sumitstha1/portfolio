from django.urls import path, include
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('appointment/', AppointmentTemplateView.as_view(), name='appointment'),
    path('manage-appointments/', ManageAppointmentTemplateView.as_view(), name='manage'),
    
    
]