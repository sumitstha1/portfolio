from re import template
from urllib import request
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect

from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings

from django.contrib import messages
from django.views.generic import ListView
from .models import Appointment
import datetime
from django.template import context
from django.template.loader import render_to_string, get_template
from .models import DoctorLogin

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        email = EmailMessage(
            subject = f"{name} from Bir Hospital.",
            body = message,
            from_email = settings.EMAIL_HOST_USER,
            to = [settings.EMAIL_HOST_USER],
            reply_to = [email]
        )
        email.send()
        return HttpResponse("Email Sent successfully")

class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            phone = mobile,
            request = message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        messages.add_message(request, messages.ERROR, f"Something Went wrong")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            'fname': appointment.first_name,
            'date': date
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment.",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()



        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name} on {date}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self,*args, **kwargs):
        if not request.session.has_key('session_email'):
            return redirect("doctor.login")
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "Manage Appointments",
        })
        return context

class DoctorLoginView(TemplateView):
    template_name = "doctorlogin.html"

    def post(self, request):
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("last_name")
        last_name = request.POST.get("middle_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        specialization = request.POST.get("specialization")

        doctor_login = DoctorLogin.objects.create(
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            email = email,
            password = password,
            specialization = specialization,
        )

        doctor_login.save()
        if request.method == 'POST':
            req_email = request.POST.get('email')
            req_password = request.POST.get('password')
            user = DoctorLogin.objects.get(email=req_email)
            if req_email == user.email and req_password == user.password:
                request.session["session_email"] = user.email
                return redirect('home')
            return render(request, template, context)

        messages.add_message(request, messages.SUCCESS, f"Thanks {first_name} for loging in...")
        return HttpResponseRedirect(request.path)

    