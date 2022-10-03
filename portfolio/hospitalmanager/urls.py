from django.urls import path, include
from . import views
from .views import DoctorLoginView, HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('appointment/', AppointmentTemplateView.as_view(), name='appointment'),
    path('manage-appointments/', ManageAppointmentTemplateView.as_view(), name='manage'),
    
    # doctor login
    path('doctorlogin/', DoctorLoginView.as_view(), name='doctor.login'),
    
]