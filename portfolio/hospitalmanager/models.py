from urllib import request
from django.db import models

# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]
        db_table = 'doctor'

class DoctorLogin(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "doctorlogin"

    