from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    img = models.FileField(null=True, blank=True)

    class Meta:
        db_table = "users"



class Patients(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    prescription = models.FileField(max_length=1000)
    profile = models.FileField(null=True, blank=True)

    class Meta:
        db_table = "patient"